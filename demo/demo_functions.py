"""
Reusable EDC demo functions for the **EDC samples connector** (the one whose
configs live in demo/connector-configs/: connector-1/2/3.properties).

Same function set as the Tractus-X variant, but adapted to the samples connector:
no management-API auth, plain localhost addresses, no docker hostname remapping.
"""

import json
import time

import httpx
import edc_client
from edc_client.api_client import ApiClient
from edc_client.rest import ApiException  # noqa: F401 — re-exported for callers

_EDC_CTX = {"@vocab": "https://w3id.org/edc/v0.0.1/ns/"}
_DSP_PROTOCOL = "dataspace-protocol-http:2025-1"


# --- Provider-side ---

def create_asset(
    client: ApiClient,
    asset_id: str,
    base_url: str,
    *,
    name: str = "Test asset",
    content_type: str = "application/json",
    proxy_path: bool = True,
) -> dict:
    """Register an HttpData asset on the provider. Returns the created asset as a dict."""
    api = edc_client.AssetV3Api(client)
    body = edc_client.AssetInputV3.from_dict({
        "@context": _EDC_CTX,
        "@id": asset_id,
        "properties": {
            "name": name,
            "contenttype": content_type,
        },
        "dataAddress": {
            "type": "HttpData",
            "name": name,
            "baseUrl": base_url,
            "proxyPath": str(proxy_path).lower(),
        },
    })
    raw = api.create_asset_v3_without_preload_content(asset_input_v3=body)
    return json.loads(raw.data)


def create_policy(
    client: ApiClient,
    policy_id: str,
    *,
    permissions: list = None,
    prohibitions: list = None,
    obligations: list = None,
) -> dict:
    """Create an ODRL policy definition. Empty lists = permissive (no constraints)."""
    api = edc_client.PolicyDefinitionV3Api(client)
    body = edc_client.PolicyDefinitionInputV3.from_dict({
        "@context": _EDC_CTX,
        "@id": policy_id,
        "policy": {
            "@context": "http://www.w3.org/ns/odrl.jsonld",
            "@type": "Set",
            "permission": permissions or [],
            "prohibition": prohibitions or [],
            "obligation": obligations or [],
        },
    })
    raw = api.create_policy_definition_v3_without_preload_content(policy_definition_input_v3=body)
    return json.loads(raw.data)


def create_contract_definition(
    client: ApiClient,
    contract_definition_id: str,
    access_policy_id: str,
    contract_policy_id: str,
    *,
    assets_selector: list = None,
) -> dict:
    """
    Link a policy to assets via a contract definition.
    assets_selector filters which assets this definition applies to — empty matches all.
    To target a specific asset: [{"operandLeft": "https://w3id.org/edc/v0.0.1/ns/id", "operator": "=", "operandRight": "<asset-id>"}]
    """
    api = edc_client.ContractDefinitionV3Api(client)
    body = edc_client.ContractDefinitionInputV3.from_dict({
        "@context": _EDC_CTX,
        "@id": contract_definition_id,
        "accessPolicyId": access_policy_id,
        "contractPolicyId": contract_policy_id,
        "assetsSelector": assets_selector or [],
    })
    raw = api.create_contract_definition_v3_without_preload_content(contract_definition_input_v3=body)
    return json.loads(raw.data)


def list_assets(client: ApiClient) -> list:
    """Return all assets registered on the provider."""
    raw = edc_client.AssetV3Api(client).request_assets_v3_without_preload_content()
    return json.loads(raw.data)


def remove_asset(client: ApiClient, asset_id: str) -> None:
    """Delete an asset. Fails with 409 if referenced by a contract agreement or active negotiation."""
    edc_client.AssetV3Api(client).remove_asset_v3(asset_id)


# --- Consumer-side ---

def fetch_catalog(
    client: ApiClient,
    counter_party_id: str,
    counter_party_address: str,
    *,
    protocol: str = _DSP_PROTOCOL,
) -> dict:
    """Fetch the provider's catalog. Returns raw JSON-LD — datasets are under 'dcat:dataset'."""
    api = edc_client.CatalogV3Api(client)
    body = edc_client.CatalogRequestV3.from_dict({
        "@context": _EDC_CTX,
        "counterPartyId": counter_party_id,
        "counterPartyAddress": counter_party_address,
        "protocol": protocol,
    })
    resp = api.request_catalog_v3_with_http_info(catalog_request_v3=body)
    return json.loads(resp.raw_data)


def negotiate(
    client: ApiClient,
    counter_party_id: str,
    counter_party_address: str,
    offer_id: str,
    asset_id: str,
    *,
    protocol: str = _DSP_PROTOCOL,
):
    """
    Initiate a contract negotiation for a specific offer.
    offer_id comes from the catalog: dataset['odrl:hasPolicy'][0]['@id'].
    Returns the raw HTTP response — parse with json.loads(raw.data)['@id'] to get the negotiation ID.
    Poll get_negotiation_v3(neg_id).state until 'FINALIZED', then read .contract_agreement_id.
    """
    api = edc_client.ContractNegotiationV3Api(client)
    body = edc_client.ContractRequestV3.from_dict({
        "@context": {
            "@vocab": "https://w3id.org/edc/v0.0.1/ns/",
            "odrl": "http://www.w3.org/ns/odrl/2/",
            # declare assigner/target as @id terms so a plain string value
            # expands to a node reference (what the connector requires),
            # while still satisfying OfferV3's string typing.
            "assigner": {"@id": "http://www.w3.org/ns/odrl/2/assigner", "@type": "@id"},
            "target":   {"@id": "http://www.w3.org/ns/odrl/2/target",   "@type": "@id"},
        },
        "@type": "ContractRequest",
        "counterPartyId": counter_party_id,
        "counterPartyAddress": counter_party_address,
        "protocol": protocol,
        "policy": {
            "@id": offer_id,
            "@type": "http://www.w3.org/ns/odrl/2/Offer",
            "assigner": counter_party_id,
            "target": asset_id,
        },
    })
    return api.initiate_contract_negotiation_v3_without_preload_content(contract_request_v3=body)


def start_pull(
    client: ApiClient,
    provider_id: str,
    counter_party_address: str,
    agreement_id: str,
    *,
    transfer_type: str = "HttpData-PULL",
    protocol: str = _DSP_PROTOCOL,
) -> dict:
    """
    Start an HttpData-PULL transfer. agreement_id comes from a finalized negotiation.
    Returns the created transfer process as a dict — use ['@id'] to get the transfer process ID.
    Poll get_transfer_state() until state is 'STARTED', then call get_edr() to get the data endpoint.
    """
    api = edc_client.TransferProcessV3Api(client)
    body = edc_client.TransferRequestV3.from_dict({
        "@context": _EDC_CTX,
        "@type": "TransferRequestDto",
        "connectorId": provider_id,
        "counterPartyAddress": counter_party_address,
        "contractId": agreement_id,
        "protocol": protocol,
        "transferType": transfer_type,
    })
    raw = api.initiate_transfer_process_v3_without_preload_content(transfer_request_v3=body)
    return json.loads(raw.data)


def start_push(
    client: ApiClient,
    provider_id: str,
    counter_party_address: str,
    agreement_id: str,
    push_destination_url: str,
    *,
    protocol: str = _DSP_PROTOCOL,
):
    """Start an HttpData-PUSH transfer. The provider will POST data to push_destination_url."""
    api = edc_client.TransferProcessV3Api(client)
    body = edc_client.TransferRequestV3.from_dict({
        "@context": _EDC_CTX,
        "@type": "TransferRequestDto",
        "connectorId": provider_id,
        "counterPartyAddress": counter_party_address,
        "contractId": agreement_id,
        "protocol": protocol,
        "transferType": "HttpData-PUSH",
        "dataDestination": {
            "type": "HttpData",
            "baseUrl": push_destination_url,
        },
    })
    return api.initiate_transfer_process_v3(transfer_request_v3=body)


def get_edr(client: ApiClient, transfer_process_id: str):
    """
    Fetch the EDR (Endpoint Data Reference) for a PULL transfer.
    Returns a DataAddress model — endpoint and authorization token are accessible via model_dump().
    Only available once the transfer state is 'STARTED'.
    """
    return edc_client.EDRCacheV3Api(client).get_edr_entry_data_address_v3(transfer_process_id)


def get_transfer_state(client: ApiClient, transfer_process_id: str):
    """Return the full transfer process model. Check .state for current status (e.g. 'STARTED')."""
    return edc_client.TransferProcessV3Api(client).get_transfer_process_v3(transfer_process_id)


def pull_data(endpoint: str, authorization: str) -> httpx.Response:
    """GET data from the EDR endpoint. Raises on non-2xx."""
    resp = httpx.get(endpoint, headers={"Authorization": authorization})
    resp.raise_for_status()
    return resp


def _edr_endpoint_auth(edr) -> tuple:
    """Pull endpoint + authorization out of an EDR DataAddress (handles plain or namespaced keys)."""
    props = edr.model_dump()
    extra = props.get("additional_properties", {}) or {}
    ns = "https://w3id.org/edc/v0.0.1/ns/"
    endpoint = props.get("endpoint") or extra.get("endpoint") or extra.get(ns + "endpoint")
    authorization = props.get("authorization") or extra.get("authorization") or extra.get(ns + "authorization")
    return endpoint, authorization


# --- End-to-end composite ---

def negotiate_and_transfer(
    client: ApiClient,
    asset_id: str,
    provider_id: str,
    counter_party_address: str,
    *,
    protocol: str = _DSP_PROTOCOL,
    poll_interval: int = 2,
    poll_timeout: int = 16,
) -> httpx.Response:
    """
    Full PULL flow: catalog → negotiate → poll agreement → start transfer → poll STARTED → fetch data.
    Returns the httpx.Response from the data plane. Use .json() or .text on the result.
    Raises ValueError if asset_id not found in catalog, TimeoutError if polling exceeds poll_timeout.
    """
    catalog = fetch_catalog(client, provider_id, counter_party_address, protocol=protocol)
    datasets = catalog.get("dcat:dataset") or catalog.get("dataset", [])
    if isinstance(datasets, dict):
        datasets = [datasets]
    dataset = next((d for d in datasets if d.get("@id") == asset_id), None)
    if not dataset:
        raise ValueError(f"Asset '{asset_id}' not in catalog. Available: {[d.get('@id') for d in datasets]}")
    policies = dataset.get("odrl:hasPolicy") or dataset.get("hasPolicy", [])
    if isinstance(policies, dict):
        policies = [policies]
    offer_id = policies[0]["@id"]

    raw = negotiate(client, provider_id, counter_party_address, offer_id, asset_id, protocol=protocol)
    neg_id = json.loads(raw.data)["@id"]

    neg_api = edc_client.ContractNegotiationV3Api(client)
    deadline = time.time() + poll_timeout
    agreement_id = None
    while time.time() < deadline:
        neg = neg_api.get_negotiation_v3(neg_id)
        if neg.state == "FINALIZED":
            agreement_id = neg.contract_agreement_id
            break
        time.sleep(poll_interval)
    else:
        raise TimeoutError("Timed out waiting for negotiation to finalize.")

    tp_id = start_pull(client, provider_id, counter_party_address, agreement_id, protocol=protocol)["@id"]

    deadline = time.time() + poll_timeout
    while time.time() < deadline:
        if get_transfer_state(client, tp_id).state == "STARTED":
            endpoint, authorization = _edr_endpoint_auth(get_edr(client, tp_id))
            return pull_data(endpoint, authorization)
        time.sleep(poll_interval)
    raise TimeoutError("Timed out waiting for transfer to start.")

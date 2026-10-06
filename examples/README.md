# examples

Hand-written, runnable usage of `edc_client` against a real EDC control plane.
Everything here is safe to edit (unlike the generated client packages). It drives
the full dataspace flow: catalog → negotiate → agreement → transfer → EDR → pull.

## The `Connector` class

`Connector` ships in the package — [`edc_client/connector.py`](../edc_client/connector.py),
`from edc_client.connector import Connector` — as a single config-driven client. The
helpers (`create_asset`, `fetch_catalog`, `negotiate`, `start_pull`, `get_edr`,
`pull_data`, …) are methods. The connector **type** is the first constructor
argument — same code, different preset, no inheritance:

- `Connector("samples", mgmt, id, protocol)` — EDC samples connector: DSP `2025-1`,
  no management auth, no EDR remap.
- `Connector("construct_x", mgmt, id, protocol, api_key)` — construct-x testbed:
  DSP `v08`, `x-api-key` auth, authed asset data addresses, EDR docker→host remap.

Override a single preset value with a keyword (`dsp_protocol=`, `asset_auth=`,
`edr_remap=`). `Connector.from_env("PROVIDER")` builds one from `PROVIDER_*` env
vars: API key set → `construct_x`, otherwise `samples`.

### Minimal usage

```python
from edc_client.connector import Connector

# one object per connector; the first argument is the type
provider = Connector("construct_x", PROVIDER_MGMT_URL, PROVIDER_ID, PROVIDER_DSP_URL, PROVIDER_API_KEY)
consumer = Connector("construct_x", CONSUMER_MGMT_URL, CONSUMER_ID, CONSUMER_DSP_URL, CONSUMER_API_KEY)

# provider: offer some data
provider.create_asset("asset-1", "https://jsonplaceholder.typicode.com/users")
provider.create_policy("policy-1")
provider.create_contract_definition("contract-def-1", "policy-1", "policy-1")

# consumer: negotiate, transfer and fetch it in one call
response = consumer.negotiate_and_transfer(provider, "asset-1")
print(response.json())
```

## Quick start

Run as modules from the repo root (`-m`, dotted path — not a file path):

```bash
python -m examples.full_flow                    # samples flavor (default)
FLAVOR=construct_x python -m examples.full_flow # construct-x
```

`FLAVOR` selects the env file (`load_env()` in [`connector.py`](connector.py));
the connector type follows from whether that file sets `*_API_KEY`:

| FLAVOR         | env file            | type            |
| -------------- | ------------------- | --------------- |
| _(unset)_      | `.env`              | `"samples"`     |
| `construct_x`  | `.env.construct_x`  | `"construct_x"` |

## Config

- [`.env`](.env) — `PROVIDER_MANAGEMENT` / `PROVIDER_PROTOCOL` / `PROVIDER_ID`,
  the same trio for `CONSUMER_*`, and `PUSH_DESTINATION_URL` (PUSH transfers only).
  construct-x adds `*_API_KEY`; see [`.env.construct_x`](.env.construct_x).
- [`connector-configs/`](connector-configs/) — EDC samples connector JAR and the
  `provider.properties` / `consumer.properties` used to launch it.

## End-to-end flow — [`full_flow.py`](full_flow.py)

Walks every step with prints:

0. Provider setup — create asset, policy, contract definition (idempotent-ish;
   re-runs 409 and continue).
1. Fetch catalog, pick the dataset + offer.
2. Initiate contract negotiation.
3. Poll negotiation until `FINALIZED`, grab the agreement id.
4. Start a PULL transfer.
5. Poll transfer until `STARTED`, fetch the EDR, pull the data.

## Per-step scripts

Standalone versions of each step, for poking at a single call. Same `-m` dotted
path, e.g. `python -m examples.negotiation.createAsset`:

- [`negotiation/`](negotiation/) — `createAsset`, `createPolicy`,
  `createContractDefinition`, `fetchCatalog`, `listAssets`, `negotiate`,
  `removeAsset`.
- [`transfer/`](transfer/) — `startTransfer`, `startPush`, `getEdr`, `pullData`,
  `getTransferState`.

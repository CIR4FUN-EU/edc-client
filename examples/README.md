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
# initialisation for two types of connectors are written below, pick one pair of connectors

# CONSTRUCT-X EDC
provider = Connector("construct_x", PROVIDER_MGMT_URL, PROVIDER_ID, PROVIDER_DSP_URL, PROVIDER_API_KEY)
consumer = Connector("construct_x", CONSUMER_MGMT_URL, CONSUMER_ID, CONSUMER_DSP_URL, CONSUMER_API_KEY)

# EDC SAMPLES CONNECTOR
provider = Connector("samples", PROVIDER_MGMT_URL, PROVIDER_ID, PROVIDER_DSP_URL)
consumer = Connector("samples", CONSUMER_MGMT_URL, CONSUMER_ID, CONSUMER_DSP_URL)

# provider: offer some data
provider.create_asset("asset-1", "https://jsonplaceholder.typicode.com/users")
provider.create_policy("policy-1")
provider.create_contract_definition("contract-def-1", "policy-1", "policy-1")

# consumer: negotiate, transfer and fetch it in one call
response = consumer.negotiate_and_transfer(provider, "asset-1")
print(response.json())
```

The consumer only needs the provider's public DSP id and address, not its management
API. Without access to the provider's connector, pass a `Counterparty` instead:

```python
from edc_client.connector import Connector, Counterparty

provider = Counterparty(PROVIDER_ID, PROVIDER_DSP_URL)
response = consumer.negotiate_and_transfer(provider, "asset-1")
```

## Quick start

The examples run against one of two connector setups, picked with the `FLAVOR` env
var. Only the samples setup is provided by this repo:

|                  | samples (default)                          | construct-x                         |
| ---------------- | ------------------------------------------ | ----------------------------------- |
| Connectors       | provided — local pair via Docker Compose   | **not provided** — bring your own   |
| Env file         | `.env`, copied from `.env.example.samples` | `.env.construct_x`, write it yourself |
| `FLAVOR`         | _(unset)_                                  | `construct_x`                       |

`load_env()` in [`connector.py`](connector.py) loads `.env.<FLAVOR>` if it exists,
else `.env`. Run everything as a module from the repo root (`-m`, dotted path — not
a file path).

### samples — everything provided

A provider + consumer pair of EDC samples connectors, started from the JAR and
`provider.properties` / `consumer.properties` in [`connector-configs/`](connector-configs/).
The example env file already points at them, so no values need changing:

```bash
cp examples/.env.example.samples examples/.env
docker compose -f examples/connector-configs/docker-compose.yml up -d
python -m examples.full_flow
```

### construct-x — bring your own connectors and config

Nothing is provided for this flavor: no connector setup and no example env file. You
need access to two running construct-x connectors and must create
`examples/.env.construct_x` yourself (ignored by git — it holds API keys):

```bash
PROVIDER_MANAGEMENT=   # management API URL
PROVIDER_PROTOCOL=     # DSP protocol URL
PROVIDER_ID=           # participant id
PROVIDER_API_KEY=      # x-api-key for the management API

CONSUMER_MANAGEMENT=
CONSUMER_PROTOCOL=
CONSUMER_ID=
CONSUMER_API_KEY=
```

```bash
FLAVOR=construct_x python -m examples.full_flow
```

`PUSH_DESTINATION_URL` is additionally needed in either env file for PUSH transfers.

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

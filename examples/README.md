# examples

Hand-written, runnable usage of `edc_client` against a real EDC control plane.
Everything here is safe to edit (unlike the generated client packages). It drives
the full dataspace flow: catalog → negotiate → agreement → transfer → EDR → pull.

## The `Connector` class

[`connector.py`](connector.py) is a single config-driven client. The demo helpers
(`create_asset`, `fetch_catalog`, `negotiate`, `start_pull`, `get_edr`,
`pull_data`, …) are methods. Two **flavors** are just different config via
classmethod presets — same code, no inheritance:

- `Connector.samples(mgmt, id, protocol)` — EDC samples connector: DSP `2025-1`,
  no management auth, no EDR remap.
- `Connector.construct_x(mgmt, id, protocol, api_key)` — construct-x testbed:
  DSP `v08`, `x-api-key` auth, authed asset data addresses, EDR docker→host remap.

## Quick start

Run as modules from the repo root (`-m`, dotted path — not a file path):

```bash
python -m examples.full_flow                    # samples flavor (default)
FLAVOR=construct_x python -m examples.full_flow # construct-x
```

`FLAVOR` selects **both** the preset and the env file (via `load_env()` /
`example_connector()` in [`connector.py`](connector.py)):

| FLAVOR         | env file            | preset                  |
| -------------- | ------------------- | ----------------------- |
| _(unset)_      | `.env`              | `Connector.samples()`   |
| `construct_x`  | `.env.construct_x`  | `Connector.construct_x()` |

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

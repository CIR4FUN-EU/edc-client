# Changelog

All notable changes to `edc-client` are documented here. The format is based on
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and this project adheres to
[Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.0] — Drop-in Client

### Added
- `edc_client.connector.Connector` — a hand-written high-level helper that wraps the
  generated API clients into an end-to-end provider/consumer flow: asset, policy and
  contract-definition creation, catalog fetch, contract negotiation, and HTTP
  push/pull transfers (including EDR retrieval and `negotiate_and_transfer()`).
- `Connector.from_env(role)` to configure a connector from environment variables.
- Runnable sample connectors with Docker Compose configs under `examples/`.

### Changed
- `get_transfer_state()` now returns the raw response.
- README links point at absolute GitHub URLs so they render on PyPI; dropped the
  inline Getting Started snippet in favour of the examples/ reference.

## [1.0.0] — Initial release

First public release of the Python client for the EDC (Eclipse Dataspace Connector)
management-api.

### Added
- `edc_client` — OpenAPI-generated client for the EDC management-api (API version 4.1.0),
  covering the v3, v4, and v5beta API groups (assets, catalog, contract definitions and
  negotiations, agreements, policy definitions, transfer processes, secrets, and more).
- Pydantic v2 request/response models and a `urllib3`-based API client.
- `py.typed` marker for type checkers.
- PEP 621 `pyproject.toml` packaging (setuptools backend) producing sdist + wheel.

[1.0.0]: https://github.com/CIR4FUN-EU/edc-client/releases/tag/v1.0.0

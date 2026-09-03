# Changelog

All notable changes to `edc-client` are documented here. The format is based on
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and this project adheres to
[Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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

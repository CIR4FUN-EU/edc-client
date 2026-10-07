"""
Env plumbing for the examples. The Connector class itself lives in the package:
edc_client/connector.py. Set FLAVOR=samples|construct_x (default samples) to
pick the env file; the connector type follows from whether an API key is set.
"""

import os

from dotenv import load_dotenv
from edc_client.connector import Connector, ApiException  # noqa: F401 — re-exported for the scripts


def active_flavor() -> str:
    return os.getenv("FLAVOR", "samples")


def load_env() -> str:
    """Load examples/.env.<FLAVOR> if it exists, else examples/.env. Returns the active flavor."""
    flavor = active_flavor()
    base = os.path.dirname(os.path.abspath(__file__))
    specific = os.path.join(base, f".env.{flavor}")
    load_dotenv(specific if os.path.exists(specific) else os.path.join(base, ".env"))
    return flavor


example_connector = Connector.from_env  # role: 'PROVIDER' or 'CONSUMER'

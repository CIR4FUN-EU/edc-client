import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from examples.connector import example_connector, load_env, ApiException

load_env()

consumer = example_connector("CONSUMER")
provider = example_connector("PROVIDER")

try:
    catalog = consumer.fetch_catalog(provider)
    print(json.dumps(catalog, indent=2))

    dataset = catalog.get("dcat:dataset") or catalog.get("dataset", {})
    if isinstance(dataset, list):
        dataset = dataset[0]
    policy = dataset.get("odrl:hasPolicy") or dataset.get("hasPolicy", {})
    if isinstance(policy, list):
        policy = policy[0]
    print(f"\nUsing offer ID: {policy.get('@id')}")
except ApiException as e:
    print(f"Error: {e.status} — {e.body}")

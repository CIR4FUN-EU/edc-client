import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from examples.connector import example_connector, load_env, ApiException

load_env()

provider = example_connector("PROVIDER")

policy_id = input("Enter a Policy ID: ").strip()

try:
    response = provider.create_policy(policy_id)
    print(json.dumps(response, indent=2))
except ApiException as e:
    print(f"Error: {e.status} — {e.body}")

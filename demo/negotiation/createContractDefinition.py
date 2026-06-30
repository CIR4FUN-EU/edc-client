import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from connector import connector, load_env, ApiException

load_env()

provider = connector("PROVIDER")

cd_id     = input("Enter a Contract Definition ID: ").strip()
policy_id = input("Enter the Policy ID to use: ").strip()

try:
    response = provider.create_contract_definition(cd_id, policy_id, policy_id)
    print(json.dumps(response, indent=2))
except ApiException as e:
    print(f"Error: {e.status} — {e.body}")

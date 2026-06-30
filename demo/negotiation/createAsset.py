import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from connector import connector, load_env, ApiException

load_env()

BASE_URL = "https://jsonplaceholder.typicode.com/users"

provider = connector("PROVIDER")

asset_id = input("Enter an Asset ID: ").strip()

try:
    response = provider.create_asset(asset_id, BASE_URL, name="product description")
    print(json.dumps(response, indent=2))
except ApiException as e:
    print(f"Error: {e.status} — {e.body}")

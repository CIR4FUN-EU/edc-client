import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from connector import connector, load_env, ApiException

load_env()

provider = connector("PROVIDER")

asset_id = input("Enter an Asset ID to remove: ").strip()

try:
    provider.remove_asset(asset_id)
    print(f"Removed asset: {asset_id}")
except ApiException as e:
    print(f"Error: {e.status} — {e.body}")

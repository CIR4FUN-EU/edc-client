import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from connector import connector, load_env, ApiException

load_env()

provider = connector("PROVIDER")

print("Assets: \n")

try:
    response = provider.list_assets()
    print(json.dumps(response, indent=2))
except ApiException as e:
    print(f"Error: {e.status} — {e.body}")

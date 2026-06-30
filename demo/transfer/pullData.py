import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from connector import Connector

endpoint      = input("Paste the endpoint from the EDR: ").strip()
authorization = input("Paste the authorization token from the EDR: ").strip()

response = Connector.pull_data(endpoint, authorization)
print(json.dumps(response.json(), indent=2))

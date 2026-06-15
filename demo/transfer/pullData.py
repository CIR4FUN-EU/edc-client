import json
import httpx

endpoint      = input("Paste the endpoint from the EDR: ").strip()
authorization = input("Paste the authorization token from the EDR: ").strip()

response = httpx.get(endpoint, headers={"Authorization": authorization})
response.raise_for_status()
print(json.dumps(response.json(), indent=2))

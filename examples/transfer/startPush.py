import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from examples.connector import example_connector, load_env, ApiException

load_env()

PUSH_DESTINATION_URL = os.environ["PUSH_DESTINATION_URL"]

consumer = example_connector("CONSUMER")
provider = example_connector("PROVIDER")

agreement_id = input("Paste the Contract Agreement ID: ").strip()

try:
    resp = consumer.start_push(provider, agreement_id, PUSH_DESTINATION_URL)
    print(f"Transfer Process ID: {resp.id}")
except ApiException as e:
    print(f"Error: {e.status} — {e.body}")

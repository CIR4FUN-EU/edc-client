import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from connector import connector, load_env, ApiException

load_env()

consumer = connector("CONSUMER")
provider = connector("PROVIDER")

agreement_id = input("Paste the Contract Agreement ID: ").strip()

try:
    tp = consumer.start_pull(provider, agreement_id)
    print(f"Transfer Process ID: {tp['@id']}")
except ApiException as e:
    print(f"Error: {e.status} — {e.body}")

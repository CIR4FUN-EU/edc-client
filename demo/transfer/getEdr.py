import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from connector import connector, load_env, ApiException

load_env()

consumer = connector("CONSUMER")

tp_id = input("Paste the Transfer Process ID: ").strip()

try:
    edr = consumer.get_edr(tp_id)
    print(json.dumps(edr.model_dump(), indent=2, default=str))
except ApiException as e:
    print(f"Error: {e.status} — {e.body}")

import json
import time
from google.cloud import pubsub_v1

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path("your-project-id", "bart-etd")

with open("sample_bart_data.json") as f:
    data = json.load(f)
    for station in data['root']['station']:
        payload = json.dumps(station).encode("utf-8")
        publisher.publish(topic_path, data=payload)
        print(f"Published station: {station['abbr']}")
        time.sleep(0.5)  # Simulate real-time intervals
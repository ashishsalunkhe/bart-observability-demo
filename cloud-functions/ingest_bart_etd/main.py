import requests
import json
from google.cloud import pubsub_v1

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path("your-project-id", "bart-etd")

def fetch_bart_etd(request):
    res = requests.get("http://api.bart.gov/api/etd.aspx?cmd=etd&orig=ALL&key=YOUR_API_KEY&json=y")
    for station in res.json()['root']['station']:
        payload = json.dumps(station).encode("utf-8")
        publisher.publish(topic_path, data=payload, station=station['abbr'])
    return "Published BART ETD records to Pub/Sub"

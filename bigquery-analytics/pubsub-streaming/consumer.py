from google.cloud import pubsub_v1
import json
import time

project_id = "gcp-de-starter-kit-491510"
subscription_id = "user-events-sub"

subscriber = pubsub_v1.SubscriberClient()
subscription_path = subscriber.subscription_path(project_id, subscription_id)

def callback(message):
    print(f"Received: {message.data.decode('utf-8')}")
    message.ack()

streaming_pull_future = subscriber.subscribe(subscription_path, callback=callback)

print("Listening to messages...")

try:
    streaming_pull_future.result()
except Exception as e:
    print(f"Error: {e}")
    streaming_pull_future.cancel()

from google.cloud import pubsub_v1
import json
import time

project_id = "gcp-de-starter-kit-491510"
topic_id = "user-events"

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_id, topic_id)

def publish_event(user_id, action):
    data = {
        "user_id": user_id,
        "action": action
    }

    message = json.dumps(data).encode('utf-8')
    future = publisher.publish(topic_path, message)

    future.result()

    print(f"Published: {data}")

# simulate event 
for i in range(5):
    publish_event(i, "click")
    time.sleep(1)

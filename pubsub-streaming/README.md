# Pub/Sub Streaming Pipeline

This module implements a simple event-driven pipeline using Google Cloud Pub/Sub.

## 📊 Architecture

Producer → Pub/Sub Topic → Subscription → Consumer

## ⚙️ Components

- **producer.py**
  - Publishes JSON messages to Pub/Sub

- **consumer.py**
  - Subscribes and processes messages in real time

## 🧪 Example Message

```json
{
  "user_id": 1,
  "action": "click"
}

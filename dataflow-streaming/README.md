# Streaming Pipeline (Pub/Sub → Dataflow → BigQuery)

This module implements a real-time data pipeline using Google Cloud.

## 📊 Architecture

Pub/Sub → Dataflow → BigQuery

## ⚙️ Input

Events published to Pub/Sub:

```json
{
  "user_id": 1,
  "action": "click"
}

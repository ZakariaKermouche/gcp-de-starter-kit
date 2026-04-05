# GCP Data Engineering Project

This repository showcases my hands-on journey building data pipelines on Google Cloud Platform.

## 🚀 Projects

### 1. Batch Analytics (BigQuery)
- Data loaded from Cloud Storage
- SQL analytics (joins, aggregations, window functions)

### 2. Streaming Pipeline (Pub/Sub)
- Event-driven architecture using Pub/Sub
- Python producer & consumer

➡️ See details: [pubsub-streaming](./pubsub-streaming)

### 3. Batch ETL Pipeline (Dataflow)

Pipeline:
Cloud Storage → Dataflow → BigQuery

Features:
- Data validation
- Data transformation
- Schema management
- Scalable processing

➡️ [Dataflow ETL Module](./dataflow-etl)

---

### 4. Streaming Pipeline (Dataflow)

Pub/Sub → Dataflow → BigQuery

- Real-time event ingestion
- Streaming processing
- Continuous data loading

➡️ [Streaming Pipeline](./dataflow-streaming)

---

## 🧱 Architecture

Batch:
CSV → Cloud Storage → Dataflow → BigQuery

Streaming
Producer → Pub/Sub → Dataflow → BigQuery

---

## 🛠️ Technologies

- GCP:
  - BigQuery
  - Pub/Sub
  - Dataflow
  - Cloud Storage
- Python
- SQL
- gcloud CLI
- Apache Beam

---


## 📌 Status

✅ Batch pipeline complete  
✅ Streaming pipeline complete  
🚀 Production-ready foundations

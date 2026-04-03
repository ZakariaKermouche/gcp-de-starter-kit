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

## 🧱 Architecture

Batch:
CSV → Cloud Storage → Dataflow → BigQuery

Streaming:
Producer → Pub/Sub → Consumer

---

## 🛠️ Technologies

- GCP (BigQuery, Pub/Sub, Dataflow, Cloud Storage)
- Python
- SQL
- gcloud CLI
- Apache Beam

---


## 📌 Status

✅ Batch ETL completed  
🚧 Next: Streaming pipeline (Pub/Sub → Dataflow → BigQuery)

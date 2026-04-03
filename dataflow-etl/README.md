# Dataflow ETL Pipeline

This module implements a batch ETL pipeline using Apache Beam on Google Cloud Dataflow.

## 📊 Architecture

Cloud Storage → Dataflow → BigQuery

## ⚙️ Input

CSV file stored in Cloud Storage:
- id
- name
- age
- country

## 🔄 Transformations

- Data validation (skip invalid rows)
- Type casting
- Business logic:
  - age < 18 → minor
  - age < 30 → young_adult
  - else → adult

## 📤 Output

BigQuery table:
`gcp_de_dataset.users_clean`

## 🧠 Concepts Demonstrated

- Apache Beam DoFn
- Batch processing
- Data validation
- Data enrichment
- Writing to BigQuery

## ▶️ How to Run

```bash
python pipeline.py

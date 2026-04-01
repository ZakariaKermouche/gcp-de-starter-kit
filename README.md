# GCP Data Engineering Foundations

This project demonstrates core Data Engineering concepts using Google Cloud Platform:

- Data ingestion via Cloud Storage
- Data warehousing with BigQuery
- Analytical SQL (joins, aggregations, window functions)

## Architecture
### Data Flow

CSV Files → Cloud Storage → BigQuery → SQL Analysis

## Technologies Used
- Google Cloud Platform (GCP)
- BigQuery
- Cloud Storage
- SQL
- Bash / gcloud CLI

## Dataset
### Users Table
- id
- name
- age

### sales Table
- order_id
- user_id
- amount
- order_date

## Key Features
- Data loaded from Cloud Storage into BigQuery
- Data modeling with relational tables
- SQL queries including:
  - Aggregations
  - Joins
  - Window functions

## Example Queries
```
-- Total spending per user
SELECT 
  u.name,
  SUM(o.amount) AS total_spent
FROM `project.dataset.users` u
JOIN `project.dataset.orders` o
ON u.id = o.user_id
GROUP BY u.name;
```

## How to Run
1. Upload CSV files to Cloud Storage
2. Load data into BigQuery
3. Run SQL queries using BigQuery or CLI

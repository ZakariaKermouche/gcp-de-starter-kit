# BigQuery Analytics Project

This module demonstrates analytical queries using Google BigQuery.

## 📊 Dataset

### Users
- id
- name
- age

### sales
- id
- user_id
- amount
- order_date

---

## ⚙️ Technologies

- Google BigQuery
- SQL
- Data Warehouse concepts

---

## 🧠 Concepts Covered

- Aggregations (SUM, AVG, COUNT)
- Joins (INNER JOIN)
- Window Functions (RANK, ROW_NUMBER)
- Grouping and filtering

---

## 🔗 Example Queries

### 1. Total Spending per User

```sql id="bq3"
SELECT 
  u.name,
  SUM(o.amount) AS total_spent
FROM `project.dataset.users` u
JOIN `project.dataset.sales` o
ON u.id = o.user_id
GROUP BY u.name;


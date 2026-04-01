bq query --use_legacy_sql=false "
SELECT 
  u.name,
  SUM(o.amount) AS total_spent,
  RANK() OVER (ORDER BY SUM(o.amount) DESC) AS rank
FROM `gcp-starter-kit-491510.gcp_de_dataset.users` u
JOIN `gcp-starter-kit-491510.gcp_de_dataset.orders` o
ON u.id = o.user_id
GROUP BY u.name
"

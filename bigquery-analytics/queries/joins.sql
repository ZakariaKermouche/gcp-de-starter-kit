bq query --use_legacy_sql=false "
SELECT 
  u.name,
  SUM(o.amount) AS total_spent
FROM `gcp-starter-kit-491510.gcp_de_dataset.users` u
JOIN `gcp-starter-kit-491510.gcp_de_dataset.sales` o
ON u.id = o.user_id
GROUP BY u.name
ORDER BY total_spent DESC
"

-- Average age:
bq query --use_legacy_sql=false "
SELECT AVG(age) AS avg_age
FROM `gcp-starter-kit-491510.gcp_de_dataset.users`
"


-- Count users:
bq query --use_legacy_sql=false "
SELECT COUNT(*) AS total_users
FROM `gcp-starter-kit-491510.gcp_de_dataset.users`
"

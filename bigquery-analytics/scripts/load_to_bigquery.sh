bq load --autodetect \
--source_format=CSV \
gcp_de_dataset.orders \
gs://gcp-de-stater-kit-zakaria-2026/users.csv


bq load --autodetect \
--source_format=CSV \
gcp_de_dataset.orders \
gs://gcp-de-stater-kit-zakaria-2026/sales.csv

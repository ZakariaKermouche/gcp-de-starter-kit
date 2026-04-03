import apache_beam as beam
from apache_beam import io
from apache_beam.options.pipeline_options import PipelineOptions


class ParseCSV(beam.DoFn):
    def process(self, element):
        fields = element.split(",")

        if len(fields) != 4:
            return

        try:
            yield {
                "id": int(fields[0]),
                "name": fields[1],
                "age": int(fields[2]),
                "country": fields[3]
            }
        except Exception as e:
            print(f"Error: {e}")


class EnrichData(beam.DoFn):
    def process(self, element):
        age = element["age"]

        if age < 18:
            age_group = "minor"
        elif age < 30:
            age_group = "young_adult"
        else:
            age_group = "adult"

        element["age_group"] = age_group
        yield element


def run():
    options = PipelineOptions(
        runner="DataflowRunner",
        project="gcp-de-starter-kit-491510",
        region="europe-west1",
        temp_location="gs://gcp-de-starter-kit-zakaria-2026/temp/",
        staging_location="gs://gcp-de-starter-kit-zakaria-2026/staging/"
    )

    with beam.Pipeline(options=options) as p:
        (
            p
            | "Read CSV" >> io.ReadFromText(
                "gs://gcp-de-starter-kit-zakaria-2026/data/users_raw.csv",
                skip_header_lines=1  # skip the CSV header row
            )
            | "Parse CSV" >> beam.ParDo(ParseCSV())
            | "Enrich Data" >> beam.ParDo(EnrichData())
            | "Write to BigQuery" >> io.WriteToBigQuery(
                table="gcp-de-starter-kit-491510:gcp_de_dataset.users_clean",
                schema={
                    "fields": [
                        {"name": "id", "type": "INTEGER"},
                        {"name": "name", "type": "STRING"},
                        {"name": "age", "type": "INTEGER"},
                        {"name": "country", "type": "STRING"},
                        {"name": "age_group", "type": "STRING"}
                    ]
                },
                write_disposition=io.BigQueryDisposition.WRITE_APPEND
            )
        )


if __name__ == "__main__":
    run()

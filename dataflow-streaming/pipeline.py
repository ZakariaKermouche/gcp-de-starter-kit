import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam import io
from apache_beam.utils import timestamp
import json

class ParseMessage(beam.DoFn):
    def process(self, element):
        data = json.loads(element.decode("utf-8"))
        print("DEBUG:", data)

        yield {
            "user_id": int(data["user_id"]),
            "action": data["action"],
            "event_time": timestamp.Timestamp.now().to_utc_datetime()
        }


def run():
    options = PipelineOptions(
        runner="DataflowRunner",
        project="gcp-de-starter-kit-491510",
        region="europe-west1",
        temp_location="gs://gcp-de-starter-kit-zakaria-2026/temp/",
        staging_location="gs://gcp-de-starter-kit-zakaria-2026/staging/",
        streaming=True
    )
    
    with beam.Pipeline(options=options) as p:

        (
            p
            | "Read from PubSub" >> io.ReadFromPubSub(
                topic="projects/gcp-de-starter-kit-491510/topics/user-events"
            )
            | "Parse JSON" >> beam.ParDo(ParseMessage())
            | "Write to BigQuery" >> io.WriteToBigQuery(
                table="gcp-de-starter-kit-491510:gcp_de_dataset.user_events",
                schema="user_id:INTEGER,action:STRING,event_time:TIMESTAMP",
                write_disposition=io.BigQueryDisposition.WRITE_APPEND
            )
        )


if __name__ == "__main__":
    run()

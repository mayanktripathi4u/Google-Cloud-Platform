import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
import logging
import re

# Read from GCS and write to BQ Table

# Args:
#     input file uri
#     output table id (dataset_id.table_id)

schema =   'jobid:STRING, scenarioid:INT64, migration_pl:FLOAT64, default_pl:FLOAT64'

class RunTimeOptions(PipelineOptions):
    @classmethod
    def _add_argparse_args(cls, parser):
        parser.add_value_provider_argument(
            "--input_file_path",
            help="uri of the input file"
        )
        parser.add_value_provider_argument(
            "--bq_table_id",
            help="dataset_id.BQ table id"
        )

class convertToDict:

    def parse_method (self, element):
        value = re.split(",", element)

        row = dict(zip(('jobid','scenarioid','migration_pl','default_pl'), value))
        return row

def run():

    data_ingestion = convertToDict()

    pipeline_options = PipelineOptions(
        streaming=False, save_main_session=True, project='gcphde-prim-dev-data', job_name='template-csv-gcs-to-bq'
    )

    pipeline = beam.Pipeline(options=pipeline_options)
    user_options = pipeline_options.view_as(RunTimeOptions)

    p =  (
        pipeline 
          | "Read From Input Datafile" >> beam.io.ReadFromText(user_options.input_file_path)
          | "Convert to Dict" >> beam.Map(lambda r: data_ingestion.parse_method(r))
          | "Write to BigQuery Table" >> beam.io.WriteToBigQuery(table=user_options.bq_table_id, schema=schema, write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND)
    )

    pipeline.run()
if __name__ == "__main__":
    logging.getLogger().setLevel(logging.INFO)
    run()



"""
To Build the template

Build the template using the following command:

 python3 -m template-csv-gcs-to-bq-04 \
 --runner DataflowRunner \
 --project gcphde-prim-dev-data \
 --staging_location gs://dataflow-handson-mayank/staging \
 --temp_location gs://dataflow-handson-mayank/temp \
 --template_location gs://dataflow-handson-mayank/templates/df_csv_gcs_to_bq \
 --experiment=use_beam_bq_sink 


 * Option --experiment=use_beam_bq_sink is required as currently dataflow overrides the BigQuery with native version which doesn’t support ValueProvider. 



Run the pipeline using template

Run the pipeline using the template by passing the uri of input CSV file and table reference in the form of dataset_id.table_id. This command will schedule the pipeline to run immediately and return the control. You can check the status of pipeline using Dataflow Console (or CLI).

 gcloud dataflow jobs run template-csv-gcs-to-bq-04 \
 --gcs-location gs://dataflow-handson-mayank/templates/df_csv_gcs_to_bq \
 --region us-central1 \
 --parameters input_file_path=gs://da_batch_pipeline/risk_test_data,bq_table_id=da_batch_pipeline.df_test_table 

"""
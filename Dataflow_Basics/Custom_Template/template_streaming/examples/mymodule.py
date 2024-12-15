import argparse
import apache_beam as beam
from apache_beam.io import WriteToBigQuery
from apache_beam.io.gcp.pubsub import ReadFromPubSub
from apache_beam.options.pipeline_options import PipelineOptions, GoogleCloudOptions, StandardOptions, SetupOptions
from apache_beam.options.value_provider import ValueProvider
import json
import re
from datetime import datetime, timedelta

class CustomPipelineOptions(PipelineOptions):
    @classmethod
    def _add_argparse_args(cls, parser):
        parser.add_value_provider_argument(
            '--input_subscription',
            help='The Cloud Pub/Sub subscription to read from.',
            type=str
        )
        parser.add_value_provider_argument(
            '--output_table',
            help='Output BigQuery table in the format: project:dataset.table',
            type=str
        )

        
def parse_pubsub_message(element):
    """Parses the Pub/Sub message into a Python dictionary."""
    try:
        return json.loads(element)
    except json.JSONDecodeError:
        return None


def transform_text(element):
    """Converts text fields to uppercase and modifies billing_status."""
    if element is None:
        return None

    # Convert all text fields to uppercase
    element['text'] = element.get('text', '').upper()

    # Modify billing_status
    billing_status = element.get('billing_status', '').lower()
    if billing_status == 'si':
        element['billing_status'] = 'Good'
    else:
        element['billing_status'] = 'Poor'

    return element


def validate_date(element):
    """Validates the date field to ensure it's not more than 30 days in the past and not in the future."""
    if element is None:
        return None

    date_str = element.get('date')
    if not date_str:
        return None

    try:
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')
        now = datetime.now()
        if now - timedelta(days=30) <= date_obj <= now:
            return element
    except ValueError:
        return None

    return None

def validate_date_v2(date_str):
    """Check if the date is within the past 30 days and not in the future."""
    current_date = datetime.datetime.utcnow().date()
    input_date = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
    if input_date > current_date:
        raise ValueError('The date is in the future.')
    if (current_date - input_date).days > 30:
        raise ValueError('The date is older than 30 days.')


def validate_email(element):
    """Validates email using a regex pattern."""
    if element is None:
        return None

    email = element.get('email', '')
    email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(email_pattern, email):
        return element

    return None


def validate_email_v2(email):
    """Simple email validation."""
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        raise ValueError(f"Invalid email address: {email}")

def transform_data_v2(element):
    """Transform the input data."""
    try:
        # Transform the text to uppercase
        element['text'] = element['text'].upper()

        # Convert billing_status
        element['billing_status'] = 'Good' if element['billing_status'] == 'si' else 'Poor'

        # Validate date
        validate_date_v2(element['date'])

        # Validate email
        validate_email_v2(element['email'])

        return element
    except Exception as e:
        # Handle or log invalid data
        print(f"Invalid data: {element}, error: {e}")
        return None
    

def run(argv=None):
    # parser = argparse.ArgumentParser()
    # parser.add_argument('--input_subscription', required=True, help='Input Pub/Sub subscription')
    # parser.add_argument('--output_table', required=True, help='Output BigQuery table in format PROJECT:DATASET.TABLE')
    # parser.add_argument('--runner', default='DataflowRunner', help='Runner type')
    # parser.add_argument('--project', required=True, help='Google Cloud project ID')
    # parser.add_argument('--region', required=True, help='GCP region')
    # parser.add_argument('--staging_location', required=True, help='GCS staging location')
    # parser.add_argument('--temp_location', required=True, help='GCS temp location')
    # parser.add_argument('--template_location', required=True, help='GCS location for the Dataflow template')

    # known_args, pipeline_args = parser.parse_known_args(argv)

#   # parser = argparse.ArgumentParser()
#   # parser.add_argument('--runner', default='DataflowRunner', help='Runner type')
#   # parser.add_argument('--project', required=True, help='Google Cloud project ID')
#   # parser.add_argument('--region', required=True, help='GCP region')
#   # parser.add_argument('--staging_location', required=True, help='GCS staging location')
#   # parser.add_argument('--temp_location', required=True, help='GCS temp location')
#   # parser.add_argument('--template_location', required=True, help='GCS location for the Dataflow template')

#   # # Use add_value_provider_argument for parameters that are passed at runtime
#   # parser.add_value_provider_argument('--input_subscription', required=True, help='Input Pub/Sub subscription')
#   # parser.add_value_provider_argument('--output_table', required=True, help='Output BigQuery table in format PROJECT:DATASET.TABLE')

#   # known_args, pipeline_args = parser.parse_known_args(argv)

#   # # Define pipeline options
#   # options = PipelineOptions(pipeline_args)
#   # google_cloud_options = options.view_as(GoogleCloudOptions)
#   # google_cloud_options.project = known_args.project
#   # google_cloud_options.region = known_args.region
#   # google_cloud_options.staging_location = known_args.staging_location
#   # google_cloud_options.temp_location = known_args.temp_location
#   # google_cloud_options.job_name = 'dataflow-custom-template-job'

#   # # Set the pipeline mode to TEMPLATE_CREATE
#   # options.view_as(StandardOptions).runner = known_args.runner
#   # options.view_as(GoogleCloudOptions).template_location = known_args.template_location

    # # Define the pipeline
    # with beam.Pipeline(options=options) as p:
    #     (
    #         p
    #         | 'Read from Pub/Sub' >> ReadFromPubSub(subscription=known_args.input_subscription)
    #         | 'Decode JSON' >> beam.Map(parse_pubsub_message)
    #         | 'Transform Text' >> beam.Map(transform_text)
    #         | 'Validate Date' >> beam.Map(validate_date)
    #         | 'Validate Email' >> beam.Map(validate_email)
    #         | 'Filter None' >> beam.Filter(lambda x: x is not None)
    #         | 'Write to BigQuery' >> WriteToBigQuery(
    #             known_args.output_table,
    #             schema='text:STRING, billing_status:STRING, date:STRING, email:STRING',
    #             create_disposition=WriteToBigQuery.CreateDisposition.CREATE_IF_NEEDED,
    #             write_disposition=WriteToBigQuery.WriteDisposition.WRITE_APPEND
    #         )
    #     )

    pipeline_options = PipelineOptions()
    pipeline_options.view_as(StandardOptions).streaming = True
    custom_options = pipeline_options.view_as(CustomPipelineOptions)

    # input_subscription = custom_options.input_subscription.get()
    # output_table = custom_options.output_table.get()

    with beam.Pipeline(options=pipeline_options) as p:
        # (
        #     p
        #     | 'Read from Pub/Sub' >> beam.io.ReadFromPubSub(subscription=custom_options.input_subscription)
        #     | 'Parse JSON' >> beam.Map(lambda x: json.loads(x.decode('utf-8')))
        #     | 'Transform data' >> beam.Map(transform_data_v2)
        #     | 'Filter out None values' >> beam.Filter(lambda x: x is not None)
        #     | 'Write to BigQuery' >> beam.io.WriteToBigQuery(
        #         custom_options.output_table,
        #         schema='text:STRING, billing_status:STRING, date:DATE, email:STRING',
        #         write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND
        #     )
        # )
        # Use a Map to convert ValueProvider to a string
        subscription = custom_options.input_subscription.get()

        (
            p
            | 'Create' >> beam.Create([None])  # Dummy PCollection to start the pipeline
            | 'Read from Pub/Sub' >> beam.FlatMap(lambda _, sub=subscription: beam.io.ReadFromPubSub(subscription=sub))  # Use FlatMap to access the subscription
            | 'Parse JSON' >> beam.Map(lambda x: json.loads(x.decode('utf-8')))
            | 'Transform data' >> beam.Map(transform_data_v2)
            | 'Filter out None values' >> beam.Filter(lambda x: x is not None)
            | 'Write to BigQuery' >> beam.io.WriteToBigQuery(
                custom_options.output_table.get(),
                schema='text:STRING, billing_status:STRING, date:DATE, email:STRING',
                write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND,
                custom_gcs_temp_location=pipeline_options.get_all_options().get('temp_location')
            )
        )

if __name__ == '__main__':
    run()
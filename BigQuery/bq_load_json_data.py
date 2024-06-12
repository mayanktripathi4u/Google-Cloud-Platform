from google.cloud import bigquery

# Construct a BQ CLient Object
client = bigquery.Client()

# Set Table_Id
table = "my-project-123.my_dataset.my_sample_table"

# Configure Job with schema defination
job_config = bigquery.LoadJobConfig(
    schema=[
        bigquery.SchemaField("product_name", "STRING"),
        bigquery.SchemaField("sold_qty", "INTEGER"),
        bigquery.SchemaField("sold_date", "DATE"),
        bigquery.SchemaField(
            "product_details", "RECORD", 
            mode="REPEATED",
            fields=(
                bigquery.SchemaField("prd_type", "STRING"),
                bigquery.SchemaField("price", "FLOAT"),
                bigquery.SchemaField("color", "STRING"),
                bigquery.SchemaField("manufacture_year", "INTEGER"),
            )
        ),
    ],
    write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE,
    source_format=bigquery.SourceFormat.NEWLINE_DELIMITED_JSON,
)

# Source JSON Data from GCS Bucket Path
uri = "gs://<full bucket path to file >/product_details.json"

# Trigger Load Job
load_job = client.load_table_from_uri(
    uri,
    table,
    location="us-central1",
    job_config=job_config
) # Make API Request

load_job.result() # Waits for the job to complete.

destination_table = client.get_table(table) 

print("{} Table has created and loaded {} rows.". format(table, destination_table.num_rows))
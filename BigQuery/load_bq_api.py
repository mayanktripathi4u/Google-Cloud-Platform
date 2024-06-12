from google.cloud import bigquery

# Construct a BQ CLient Object
client = bigquery.Client()

# Set Table_Id
table = "my-project-123.my_dataset.my_sample_table"

job_config = bigquery.LoadJobConfig(
    skip_leading_rows = 1,
    # The source format default to CSV 
    source_format = bigquery.SourceFormat.CSV,
)

url = "gs://<path to csv file on cloud storage bucket>"

load_jobs = client.load_table_from_uri(
    url, table, job_config=job_config
) # Make API Call

load_jobs.result() # Waits for the job to complete.

destination_table = client.get_table(table) 

print("Loaded {} rows.". format(destination_table.num_rows))
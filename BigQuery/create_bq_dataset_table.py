from google.cloud import bigquery

# Construct a BQ CLient Object
client = bigquery.Client()

# Dataset Creation
# Set dataset_id to ID of the dataset to create
dataset_id = "{}.demo_dataset_api".format(client.project)

# COnstruct a full dataset object to send to API
dataset = bigquery.Dataset(dataset_id)

# Specifiy the Geography location where the dataset should reside
dataset.location="us-central1"

# Send the dataset to API for creation
dataset = client.create_dataset(dataset=dataset, timeout=30) # Makes an API Request
print(f"Dataset {dataset.dataset_id} is created in project {client.project}")

# Table Creation
# Set the table_id to the ID of the table to create.
table_id = f"{client.project}.{dataset.dataset_id}.my_sample_tbl_viaAPI"

schema = [
    bigquery.SchemaField("year", "STRING", mode="NULLABLE"),
    bigquery.SchemaField("category", "STRING", mode="NULLABLE"),
    bigquery.SchemaField("value", "FLOAT", mode="NULLABLE"),
]

table = bigquery.Table(table_id, schema=schema)
table = client.create_table(table=table) # Make an API request

print(f"Table Created. {table.project} {table.dataset_id} {table.table_id}")
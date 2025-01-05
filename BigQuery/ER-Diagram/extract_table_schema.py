from google.cloud import bigquery

print(f"extract table schema process initiated!")

# Initialize the BigQuery client
client = bigquery.Client()

def get_bigquery_schema(project_id, dataset_id):
    print(f".......get_bigquery_schema function called.......")
    dataset_ref = client.dataset(dataset_id, project=project_id)
    tables = client.list_tables(dataset_ref)  # List all tables in the dataset
    table_schemas = {}

    for table in tables:
        print(f"Running loop for table: {table}, to fetch schema.")
        table_ref = dataset_ref.table(table.table_id)
        schema = client.get_table(table_ref).schema  # Get the schema for each table
        table_schemas[table.table_id] = [field.name for field in schema]  # Store column names

    return table_schemas

# Set Variables.
project_id = 'gcphde-prim-dev-data'
dataset_id = 'sample_dataset'
schemas = get_bigquery_schema(project_id, dataset_id)

# Print the schema of all tables
for table_name, columns in schemas.items():
    print(f"Table: {table_name}")
    for column in columns:
        print(f"  - {column}")


import json
import logging
import os
import traceback
import re
from google.cloud import storage, bigquery
import yaml

with open("/Users/tripathimachine/Desktop/Apps/GitHub_Repo/Google-Cloud-Platform/BigQuery/LoadDataFromGCS/schemas.yaml") as schema_file:
    config = yaml.load(schema_file, Loader = yaml.Loader)

# # Set Key credentials file path when using SA
# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/tripathimachine/Desktop/Apps/GitHub_Repo/Google-Cloud-Platform/BigQuery/LoadDataFromGCS/jsonk-key-for-sa.json"

PROJECT_ID = os.getenv("")
print(f"Identified the Project as {PROJECT_ID} based on the evn.")
BQ_DATASET = 'dataset_3'
GCS = storage.Client()
BQ = bigquery.Client()

job_config = bigquery.LoadJobConfig()

def streaming(data, context):
    bucketname = data['bucket']
    print("Bucket Name", bucketname)
    filename = data['name']
    print("File Name", filename)
    timeCreated = data['timeCreated']
    print("Time Created", timeCreated)

    print(f"config : {config}")
    try:
        for table in config:
            tableName = table.get('name')
            print(f"TableName {tableName} retrived from config.")
            print(re.search(tableName, filename))
            print(tableName.replace('_', '-'))
            print(re.search(tableName.replace('_', '-'), filename))

            if re.search(tableName.replace('_', '-'), filename) or re.search(tableName, filename):
                tableSchema = table.get('schema')
                _check_if_table_exists(tableName, tableSchema)
                tableFormat = table.get("format")
                if tableFormat == "NEWLINE_DELIMITED_JSON":
                    _load_table_from_uri(data['bucket'], data['name'], tableSchema, tableName)
    except Exception:
        print("Error streaming file. Cause: %s" %(traceback.format_exc()))

def _check_if_table_exists(tableName, tableSchema):
    table_id = BQ.dataset(BQ_DATASET).table(tableName)

    try:
        BQ.get_table(table_id)
    except Exception:
        logging.warn('Creating tbale: %s' %(tableName))
        schema = create_schema_from_yaml(tableSchema)
        table = bigquery.Table(table_id, schema=schema)
        table = BQ.create_table(table=table)
        print("Created Table {}.{}.{}".format(table.project, table.dataset_id, table.table_id))

def create_schema_from_yaml(table_schema):
    schema = []
    for column in table_schema:
        schemaField = bigquery.SchemaField(column['name'], column['type'], column['mode'])
        schema.append(schemaField)

        if column['type'] == 'RECORD':
            schemaField._fields = create_schema_from_yaml(column['field'])

    return schema

def _load_table_from_uri(bucket_name, file_name, tableSchema, tableName):
    uri = 'gs://%s/%s' % (bucket_name, file_name)
    table_id = BQ.dataset(BQ_DATASET).table(tableName)
    
    schema = create_schema_from_yaml(table_schema=tableSchema)
    print(schema)
    job_config.schema = schema

    job_config.source_format = bigquery.SourceFormat.NEWLINE_DELIMITED_JSON,
    job_config.write_disposition = 'WRITE_APPEND',

    load_job = BQ.load_table_from_uri(
        uri,
        table_id,
        job_config=job_config,
    )

    load_job.result()
    print("Job FInished Successfully")


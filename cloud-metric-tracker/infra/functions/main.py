import os
import pandas as pd
from google.cloud import storage, bigquery

pd.set_option('display.max_columns', None)

def process_csv(event, context):
    client = storage.Client()
    bucket_name = event['bucket']
    blob_name = event['name']

    print(f"1. -----> Reading the file {blob_name} from Bucket {bucket_name}")
    
    bucket = client.get_bucket(bucket_name)
    blob = bucket.blob(blob_name)
    
    print(f"2. -----> Reading the file {blob} from Bucket {bucket}")

    # df = pd.read_csv(blob.download_as_text())

    local_path = f"/tmp/{blob_name}"
    colnames=['index','cloud_provider','vp_group','category','subscription','rate', 'avoidance', 'trend','notes'] 

    blob.download_to_filename(local_path)

    df = pd.read_csv(local_path, names=colnames, header=0, dtype={'index': 'object'})
    
    print("3. ------> DataFrame Created.")
    # print(df.head())
    print("3.1. ------> DataFrame First Row.")
    print(df.iloc[:1])

    # df[['rate', 'avoidance', 'trend']] = df['recognized'].str.split(',', expand=True)
    # print("3.5. ------> DataFrame After Split of recognized.")
    # print(df.head())
    # print(df.iloc[:1])

    

    # df = df.drop(columns=['recognized'])

    # print("4. ------> Dropped recognized column from DataFrame.")
    # print(df.head())
    
    bq_client = bigquery.Client()
    table_id = f"{os.getenv('GOOGLE_CLOUD_PROJECT')}.{os.getenv('BQ_DATASET')}.{os.getenv('BQ_TABLE')}"
    
    job = bq_client.load_table_from_dataframe(df, table_id)
    job.result()

    print("5. ------> Data Loaded into BigQuery.")

    print(f"Loaded {df.shape[0]} rows into {table_id}.")

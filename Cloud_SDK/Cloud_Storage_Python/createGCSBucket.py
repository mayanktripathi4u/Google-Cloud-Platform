# Import Packages
from google.cloud import storage
import os

# Set Key Credentials File Path, if using Service Account.
# os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "<path to service account key in json format>"

# Define the FUnction
def create_bucket(bucket_name, storage_class = 'STANDARD', location="us-central1"):
    storage_client = storage.Client()

    bucket = storage_client.bucket(bucket_name=bucket_name)
    bucket.storage_class = storage_class

    bucket = storage_client.create_bucket(bucket, location=location)

    return f"Bucket {bucket.name} successfully created!"

## Invoke Function
res = create_bucket("my_bucket1234_31july")
print(res)


# Import Packages
from google.cloud import storage
import os

# Set Key Credentials File Path, if using Service Account.
# os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "<path to service account key in json format>"

# Define the FUnction to list the objects / files in a bucket
def list_files_in_bucket(bucket_name):
    storage_client = storage.Client()

    files_list = storage_client.list_blobs(bucket_name)
    files_list = [file.name for file in files_list]

    return files_list

## Invoke Function
res = list_files_in_bucket("my_bucket1234_31july")
print(res)
# Import Packages
from google.cloud import storage
import os

# Set Key Credentials File Path, if using Service Account.
# os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "<path to service account key in json format>"

# Define the FUnction
def upload_to_gcs(bucket_name, source_file_name, destination_file_name):
    storage_client = storage.Client()

    bucket = storage_client.bucket(bucket_name=bucket_name)
    
    blob = bucket.blob(destination_file_name)
    blob.upload_from_filename(source_file_name)

    return True

# Invoke the Function
upload_to_gcs("my_bucket1234_31july", "Google-Cloud-Platform/Cloud_SDK/Cloud_Storage_Python/sample.txt", "python_skd/sample_renamed.txt")



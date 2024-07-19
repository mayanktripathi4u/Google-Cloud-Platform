# Get the list of files and folders in a given Bucket 
## Using Cloud Storage CLI
```
gsutil ls gs://mybucket
```
Note: You should use `gcloud storage` commands instead of `gsutil` commands: The `gsutil` tool is a legacy Cloud Storage CLI and minimal maintained. The `gsutil` tool does not support working with newer Cloud Storage features, such as soft delete and managed folders. --> As per [Google Docs](https://cloud.google.com/storage/docs/gsutil)

## using Google Cloud API / Cloud SDK
``` main.py
from google.cloud import storage
#import google.cloud.storage as gcs

# Instantiates a Client
client = storage.Client()

bucket_name = "mybucketname"

# Get GCS Bucket
bucket = client.get_bucket(bucket_name)

# Get blobs in bucket (including subdir)
blobs_all = list(bucket.list_blobs())

# Get blobs in specific directory
blobs_specific = list(bucket.list_blobs(prefix = 'path/to/subfolder/'))
```

```
PROJECT_NAME = "my-gcp-project"
BUCKET_NAME = "mybucket"

from google.oauth2.service_account import Credentials
import google.cloud.storage as gcs

client = gcs.client(
    project = PROJECT_NAME,
    credentials = Credentials.from_service_account_file("/myjsonkey.json"),
)

blobs = client.list_blobs(
    BUCKET_NAME,
    prefix="abc/", # trailing slash is required
    delimiter="/",
    max_results=1,
)
```
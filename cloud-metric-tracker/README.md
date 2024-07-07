To set up an end-to-end data pipeline on Google Cloud using Terraform, we will follow these steps:

1. Create a Cloud Storage Bucket
2. Set up a BigQuery Dataset and Table
3. Deploy a Cloud Function to Process CSV Files
4. Configure Cloud Storage to Trigger the Cloud Function
5. Use Terraform to Manage Infrastructure

## Step 1: Create a Cloud Storage Bucket
We need to create a Cloud Storage bucket to store the incoming CSV files. This can be done using Terraform.

## Step 2: Set up a BigQuery Dataset and Table
Create a BigQuery dataset and table. The schema for the table will be defined in a separate JSON file.

## Step 3: Deploy a Cloud Function to Process CSV Files
The Cloud Function will be triggered when a file is uploaded to the Cloud Storage bucket. It will read the CSV file, convert it to a pandas DataFrame, and then load it into the BigQuery table.

## Step 4: Configure Cloud Storage to Trigger the Cloud Function
Set up a notification on the Cloud Storage bucket to trigger the Cloud Function upon new file uploads.

## Step 5: Use Terraform to Manage Infrastructure
We will use Terraform to create and manage all the resources.

### Terraform Configuration
1. Terraform Setup
Create a main Terraform configuration file [main.tf](./infra/main.tf).

2. BigQuery Schema
Create the schema file [bq_schema.json](./infra/schemas/bq_schema.json).

3. Cloud Function Code
Create the Cloud Function code in [main.py](./infra/functions/main.py)
Create a [requirements.txt](./infra/functions/requirements.txt) for the Cloud Function dependencies.

## Deploying with Terraform
1. Initialize Terraform:
```
terraform init
```

2. Apply the Configuration:
```
terraform apply
```

# Conclusion
This setup will create a Cloud Storage bucket, a BigQuery dataset and table, and a Cloud Function. The Cloud Function will be triggered whenever a new CSV file is uploaded to the Cloud Storage bucket, parse the CSV file, and load it into the BigQuery table.


# Test
Upload the sample file to GCS Bucket
```
gsutil cp data/sample_cloud_matrix_tracker.csv gs://cloud-metric-tracker/
```



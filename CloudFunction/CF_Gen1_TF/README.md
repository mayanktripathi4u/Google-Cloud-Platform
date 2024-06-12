# Deploy Cloud Functions on GCP with Terraform (1st Gen Environment)
How to set up a Cloud Function in Google Cloud Platform (GCP) that is triggered whenever a file is uploaded to a specific Google Cloud Storage (GCS) bucket.

## We’ll focus on deploying the following resources using Terraform:

* Bucket for file uploads: This is a Google Cloud Storage bucket that will be used to upload files to. It provides a scalable and durable storage solution for storing files.
* Bucket for Cloud Function source code: This is another Google Cloud Storage bucket that will store the source code for the Cloud Function. The Cloud Function will be triggered by file uploads to the first bucket.
* Cloud Function: This is a serverless function that runs in response to events, in this case, a file upload event to the first bucket. The Cloud Function is written in code (e.g., Python) and is stored in the second bucket. It allows you to perform custom logic or processing on the uploaded files, such as generating thumbnails, processing data, or sending notifications.

### Folder Structure:
* `src` folder contains the Python source code of the cloud function
* `terraform` folder contains the configuration files

### Create Python function:
[src/main.py](/GCP/CloudFunctions/CF_Gen1_TF/src/main.py)

The fileUpload function is the entry point of the Cloud Function. It takes two parameters: event and context. The event parameter contains information about the file upload event, such as the bucket name, file name, and file size. You can extract and use this information in your function.

[requirements.txt](): the list of python libraries required by main.py to run.

### Create Terraform Infrastructure:
provider.tf: To declare the connection to the Google provider in Terraform, you need to specify the provider block in your Terraform configuration file.

backend.tf: To configure the backend for storing and retrieving the Terraform state.

variables.tf: Declare the variables used in the Terraform files.

storage-bucket.tf: Cloud Storage buckets to store the code of the Cloud Function and to upload files.

cloudfunction.tf: Declare the Cloud Function.

### Deploy cloud function:
Start with initializing the Terraform workspace. Aterraform initdownloads all the required providers and plugins. Run a Terraform plan creates an execution plan. The execution plan looks good, so let’s move ahead and apply this plan.

        cd terraform
        terraform init
        terraform fmt
        terraform validate
        terraform apply -auto-approve


## To test if everything is working correctly, follow these steps:
1. Open the Google Cloud Console and log in to your project.
2. Navigate to the Google Cloud Storage browser.
3. Click on the bucket named input-<YOUR-PROJECT-ID>.
4. Upload any file into the bucket to trigger the Cloud Function.
5. To verify that the Cloud Function was triggered, go to the Cloud Functions list in the Google Cloud Console.

This test ensures that the Cloud Function is successfully triggered whenever a file is uploaded to the specified bucket, and you can confirm its execution by checking the logs.

Destroy: To destroy Terraform-provisioned infrastructure.
        terraform destroy --auto-approve


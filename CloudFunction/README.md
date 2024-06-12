# Cloud Function
Cloud Function are serverless and Environment free.

They supports events such as HTTP, Cloud Storage, Cloud Firestore, Pub/Sub, Firebase, Stackdriver.

Cloud Functions is a serverless computing service provided by cloud platforms that allows you to run your code without the need to manage servers. It is a lightweight computing solution for developers to create single-purpose, stand-alone functions that respond to Cloud events without the need to manage a server or runtime environment. With Cloud Functions, you can write small, single-purpose functions in languages like Python, Node.js, Go, Java, .NET, Ruby, and PHP, and have them executed in response to events or HTTP requests.

# Prerequisites
* Terraform installed on your local machine
* Google Cloud SDK installed on your local machine
* Google Cloud Platform project set up
* Enable the Cloud Functions API

# Cloud Function with Pub/Sub Trigger
It supports multiple languages such as Java, Python, Ruby, Nodes.js, GO, and .Net

Step 1: Create a Pub/Sub Topic from Console.
    Say Tpoic Name: "send-messages"
    From Pub/Sub topic page itself we have a option to create and link Cloud Function.

Step 2: Create Cloud Function
    Trigger: Pub/Sub Topic.
    
# Deploy Cloud Functions on GCP with Terraform (1st Gen Environment)
How to set up a Cloud Function in Google Cloud Platform (GCP) that is triggered whenever a file is uploaded to a specific Google Cloud Storage (GCS) bucket.

Refer the [code at](/GCP/CloudFunctions/CF_Gen1_TF/README.md)
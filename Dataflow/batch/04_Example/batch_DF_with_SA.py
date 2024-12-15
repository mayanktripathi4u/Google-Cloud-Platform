from google.auth.transport.requests import Request
from google.auth import exceptions
from googleapiclient.discovery import build
from google.oauth2 import service_account

def create_dataflow_job(project_id, region, service_account_email, job_name):
    try:
        # Define the Dataflow client
        service = build('dataflow', 'v1b3')

        # Specify the template parameters
        job_config = {
            "jobName": job_name,
            "environment": {
                "serviceAccountEmail": service_account_email,
                "tempLocation": "gs://dataflow-handson-mayank/temp/",  # Specify the GCS temp location
                "zone": "us-east-4",  # Optional, specify the zone
                "maxWorkers": 5,  # Optional, specify the maximum number of workers
            },
            "parameters": {
                "inputFile": "gs://dataflow-handson-mayank/input/input-file.csv",  # Input file in GCS
                "outputFile": "gs://dataflow-handson-mayank/output/output-file",  # Output file in GCS
            }
        }

        # Construct the request to create the job
        request = service.projects().locations().templates().launch(
            projectId=project_id,
            location=region,
            body=job_config
        )

        # Execute the request to create the job
        response = request.execute()

        # Display the response (includes job details)
        print("Job Created Successfully!")
        print(f"Job Name: {response['job']['name']}")
        print(f"Service Account: {service_account_email}")
        print(f"Status: {response['job']['currentState']}")

        return response

    except exceptions.GoogleAuthError as auth_error:
        print(f"Authentication Error: {auth_error}")
    # except exceptions.GoogleAPIError as api_error:
        # print(f"API Error: {api_error}")
    except Exception as e:
        print(f"Error occurred: {e}")

# Example usage
project_id = "gcphde-prim-dev-data"
region = "us-east-4"  # Specify the region
service_account_email = "dataflow-runner@gcphde-prim-dev-data.iam.gserviceaccount.com"
job_name = "my-dataflow-job-with-sa"

create_dataflow_job(project_id, region, service_account_email, job_name)

# Dataflow job with a service account
To create a Dataflow job with a service account in Google Cloud, you need to specify the service account in the environment configuration while creating the job. The service account is used to run the Dataflow job and can be set when you're configuring the job.

Here’s a step-by-step guide on how to create a Dataflow job with a specific service account using the Python google-api-python-client library.

# Prerequisites:
1. Ensure that you have the correct service account in your Google Cloud project with the necessary permissions.
   * The service account should have permissions like roles/dataflow.worker and other necessary roles to interact with your data sources and sinks.

2. Install the required Python libraries
```bash
pip install google-api-python-client google-auth google-cloud
```

# Steps to Create a Dataflow Job with a Service Account:
* Step 1: Define Job Configuration and Service Account
When creating a Dataflow job, you'll define the job's configuration in the request payload. The service account is specified under the `serviceAccountEmail` field within the `environment` section.

* Step 2: Python Code to Create the Dataflow Job
[code](/Google-Cloud-Platform/Dataflow/batch/04_Example/batch_DF_with_SA.py)

  * Key Points:
    * Service Account: The serviceAccountEmail field is specified under the environment section. This tells Dataflow to run the job with the given service account.
    * Temporary Location: You must specify a GCS location for temporary files (tempLocation), which is required by Dataflow.
    * Job Parameters: You can pass custom parameters as needed for your Dataflow job (e.g., input/output files).
    * Job Launch: We use the launch() method to create and run the Dataflow job from a template. This can be customized to use various types of templates (e.g., pre-built, custom, or Flex templates).

* Step 3: Permissions for the Service Account
Ensure that the service account you're using has the necessary IAM roles. At a minimum, it should have:

  * `roles/dataflow.worker` for running Dataflow jobs.
  * `roles/storage.objectAdmin` (or equivalent) if interacting with Google Cloud Storage.
  * Any other roles required for reading from and writing to your input and output sources.

* Step 4: Verify the Job and Check Status
Once the job is created, you can monitor it via the Google Cloud Console, under the Dataflow section. Additionally, you can query the job status using the get method from the `google-api-python-client` as previously shown.

Example Response:
If the job is created successfully, you should get a response like this:
```json
{
  "job": {
    "name": "projects/your-gcp-project-id/locations/us-central1/jobs/your-dataflow-job-id",
    "currentState": "JOB_STATE_RUNNING",
    "serviceAccountEmail": "your-service-account@your-gcp-project-id.iam.gserviceaccount.com"
  }
}
```

This confirms that the job has been created and is running with the specified service account.

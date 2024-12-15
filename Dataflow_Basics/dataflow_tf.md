# Google Cloud Dataflow with Terraform

## What is `dataflow` in GCP?
Google Cloud Dataflow is a managed service for processing and transforming large datasets in real-time or batch mode. It's built on Apache Beam, an open-source unified programming model that allows you to write pipelines for data processing, which can be executed across different backends. Dataflow automates resource management, optimization, and scaling, making it ideal for large-scale data processing tasks.

### What is Dataflow Used For?
* **Data Ingestion** and **ETL** (Extract, Transform, Load): Dataflow is often used to clean, transform, and load data from various sources (like databases, cloud storage, or streaming services) into data warehouses such as BigQuery.
* **Real-Time Data Processing:** It can handle streaming data in real-time, making it suitable for applications like event monitoring, fraud detection, and live analytics.
* **Batch Data Processing:** Dataflow can also process static datasets stored in cloud storage for tasks such as data migration or periodic report generation.

### Key Variants/Features in Google Cloud Dataflow
1. Streaming Dataflow Jobs
   * Real-Time Processing: These jobs are used for real-time data processing, where data is continuously ingested and processed as it arrives.
   * Use Cases: Stream analytics, log monitoring, live dashboards, real-time fraud detection.
   * Windowing and Triggers: Dataflow provides mechanisms for handling out-of-order data through windowing (grouping data by time) and triggers (defining when results should be output).
2. Batch Dataflow Jobs
   * Processing Historical Data: Batch jobs are used for processing static datasets that are stored in places like Google Cloud Storage or BigQuery.
   * Use Cases: ETL pipelines, daily report generation, data archiving.
   * Cost Management: Suitable for workloads where you can trade off real-time results for cost savings, as batch processing can be optimized for lower costs.
3. Flex Templates
   * Custom and Dynamic Pipelines: Flex Templates allow users to package custom Docker containers for their Dataflow jobs. This is helpful when you need to use libraries or dependencies that aren't supported in the default Dataflow environment.
   * Flexibility in Configurations: Flex Templates enable defining pipeline parameters dynamically, making them more versatile than classic templates.
   * Use Cases: Suitable for jobs that require custom execution environments or configurations that are adjusted frequently.
4. Classic Templates
   * Pre-Built Templates for Reusability: Classic templates are a simpler way to run Dataflow jobs. They are pre-packaged and stored in Google Cloud Storage, allowing users to run the same job multiple times with different input parameters.
   * Less Flexibility Compared to Flex Templates: Classic templates are not as customizable as Flex Templates since they don't support Docker images.
5. Auto-scaling and Dynamic Work Rebalancing
   * Auto-scaling: Dataflow can automatically scale the number of workers up or down based on the workload, optimizing for cost and performance.
   * Dynamic Work Rebalancing: During a job, Dataflow can rebalance the distribution of work across workers to ensure even load distribution.

### Summary
* `Google Cloud Dataflow` provides a powerful way to process data at scale, offering real-time streaming and batch processing capabilities.
* **Variants include**:
  * `Streaming` vs. `Batch Dataflow Jobs`: For real-time data vs. historical/static data processing.
  * `Flex Templates` vs. `Classic Templates`: For more customizable and dynamic pipeline execution vs. reusing pre-packaged templates.
* Additional features like auto-scaling, windowing, triggers, and dynamic work rebalancing make it a flexible and efficient choice for data processing needs.

## Diffeence between terraform resource "google_dataflow_job" Vs resource "google_dataflow_flex_template_job"

The google_dataflow_job and google_dataflow_flex_template_job resources in Terraform are both used to create and manage Dataflow jobs in Google Cloud, but they differ in how they define and execute the job.

### google_dataflow_job
**Usage**: The google_dataflow_job resource is used to create a Dataflow job directly from a pre-built Apache Beam pipeline JAR file or Python script. It is suitable for scenarios where the pipeline code is already compiled and available as a template file or script.

**Key Characteristics:**
* Requires the pipeline code (JAR or Python file) to be provided along with other configurations like staging location, parameters, and worker settings.
* Uses "classic" templates, which are defined in Apache Beam and can be stored in a GCS location.
* Suitable for older use cases where the job is started from a classic template or a fully built JAR/Python file.
* Example Configuration
```bash
resource "google_dataflow_job" "example" {
  name       = "example-job"
  template_gcs_path = "gs://my-bucket/templates/my-template"
  temp_gcs_location = "gs://my-bucket/temp"

  parameters = {
    inputFile  = "gs://my-bucket/input-data.csv"
    outputFile = "gs://my-bucket/output-data.csv"
  }
}
```
* The above example uses a Dataflow job template stored in a GCS bucket.


### google_dataflow_flex_template_job
**Usage**: The google_dataflow_flex_template_job resource is used to create Dataflow jobs using Flex Templates. Flex Templates allow for more flexibility and customization in defining Dataflow jobs compared to classic templates.

**Key Characteristics:**
* Uses Docker images to package the job's Apache Beam pipeline code. This allows for greater customization of the runtime environment and dependencies.
* Flex Templates can be built and deployed more dynamically, with configurations defined at runtime.
* Suitable for newer Dataflow use cases where the environment customization, parameterization, and Docker-based packaging are required.
* Allows specifying a template file stored in GCS, which contains the job specification.
* Example Configuration:
```bash
resource "google_dataflow_flex_template_job" "example" {
  name           = "example-flex-job"
  template_gcs_path = "gs://my-bucket/flex-templates/my-flex-template.json"
  parameters = {
    inputFile  = "gs://my-bucket/input-data.csv"
    outputFile = "gs://my-bucket/output-data.csv"
  }

  environment {
    temp_gcs_location = "gs://my-bucket/temp"
    machine_type      = "n1-standard-4"
  }
}
```
* In this example, the job is defined using a Flex Template JSON file stored in GCS, providing runtime flexibility.

### Key Differences
|**Aspect**	|**google_dataflow_job**	|**google_dataflow_flex_template_job**|
|-------|-----------------------|---------------------------------|
|Template Type	|Uses classic templates (pre-built JAR or Python script).	|Uses Flex Templates (Docker-based and customizable).|
|Customization	|Limited customization for runtime environments.	|Allows using custom Docker images and dynamic configurations.|
|Usage Scenario	|Suitable for existing classic templates or simple jobs.	|Recommended for more complex pipelines requiring custom environments.|
|Template Definition	|Provided directly as JAR/Python file path or GCS template.	|Uses a JSON specification file stored in GCS.|
|Environment Flexibility	|Less flexible for dependency management.	|More flexible due to the use of Docker containers.|


### When to Use Which
* Use google_dataflow_job when you have existing classic Dataflow templates and don't need the extra flexibility provided by Flex Templates.
* Use google_dataflow_flex_template_job if you need custom environments, want to use Docker images, or require dynamic configuration at runtime.

Flex Templates provide a modern approach with more options for customizing Dataflow jobs, making them suitable for new projects and more complex use cases.


In the terraform resource `google_dataflow_job` what does the parameter `template_gcs_path = "gs://my-bucket/templates/my-template"` indicates... explain in layman terms.
Also for the same TF resource, it Requires the pipeline code (JAR or Python file) to be provided.. what exactly this means.

# Concern-1:
In the Terraform resource google_dataflow_job, the parameter template_gcs_path = "gs://my-bucket/templates/my-template" specifies the location of a Dataflow job template stored in a Google Cloud Storage (GCS) bucket. Let's break it down in simple terms:

## What is `template_gcs_path`?
* **Template Location:** The template_gcs_path is a path to a file in a GCS bucket. In this example, "gs://my-bucket/templates/my-template" refers to a template file located in a GCS bucket named "my-bucket" in the "templates" folder, with the file name "my-template."
* **Purpose of the Template:** The template is essentially a pre-configured Dataflow job that contains instructions for how the job should run. It includes details about the processing pipeline, which specifies how data should be read, transformed, and output.
* **Why Use a Template?** By using a template, you can run a Dataflow job without having to write or compile the code every time. Instead, you deploy the template and provide parameters for each run.

## What Does "Requires the Pipeline Code" Mean?
* **Pipeline Code Explained:** In the context of Dataflow, a "pipeline" is a set of instructions for processing data. For example, it might read data from a source, transform it (e.g., filter or modify data), and then write it to a destination. The pipeline is usually written using Apache Beam, which supports programming languages like Java and Python.
* **Providing the Code:** When you create a Dataflow job, you first need to write the code that defines how the data will be processed. This code is typically packaged into a file (such as a JAR file for Java or a Python script for Python). You then create a "template" from this code, which can be uploaded to GCS.
* **Using the Template:** When you run a Dataflow job with Terraform using the google_dataflow_job resource, you reference the location of this template in GCS with the template_gcs_path. Terraform will then launch a Dataflow job using the pre-defined pipeline code stored in that template.

### In Layman's Terms
* Imagine you have a recipe (the template) stored in a cloud storage (GCS) that tells a chef (Dataflow) how to cook a dish (process data).
* You create this recipe by writing the cooking steps (the pipeline code), and then you save it in the cloud storage as a template.
* When you want to run the job (cook the dish), you tell Dataflow where to find the recipe (template_gcs_path), and it follows the instructions in the recipe to prepare the dish.
* The pipeline code is like the original written instructions for the recipe, and the template is a saved version of it that can be reused multiple times.

In summary, template_gcs_path indicates the location of a saved Dataflow job template in GCS, and the pipeline code is the original set of instructions used to create that template.

# Concern-2
The `template_gcs_path` is a path to a file in a GCS bucket. In the given example, `"gs://my-bucket/templates/my-template"` refers to a template file located in a GCS bucket named `"my-bucket"` in the `"templates"` folder, with the file name `"my-template."`
what exactly does it has... is it a python script.. or what? Provide an complete example.

The `template_gcs_path` in a Google Cloud Dataflow job points to a Dataflow template, not directly to a Python script or JAR file. A Dataflow template is a pre-configured, packaged pipeline that specifies how the data processing job should run. It is created from your pipeline code, which can be written in Apache Beam using Java or Python.

## What is a Dataflow Template?
A Dataflow template is essentially a snapshot of a pipeline that has been compiled and uploaded to Google Cloud Storage (GCS). This template contains all the necessary configurations for executing the pipeline without requiring the original code to be provided at runtime. There are two main types of templates:

1. Classic Templates: These are static and do not support dynamic configurations beyond what was defined when the template was created.
2. Flex Templates: These offer more flexibility by allowing you to package custom Docker containers and adjust parameters dynamically.
   
## Creating a Dataflow Template: Example
Let's walk through creating a Dataflow template using a Python Apache Beam pipeline and uploading it to GCS.

**Step 1:** Write a Simple Apache Beam Pipeline (Python)
Here's a basic example of a Python script (my_pipeline.py) that reads lines from a text file in GCS, transforms the lines to uppercase, and writes the output to another GCS location.
```bash
import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions

class UpperCaseTransform(beam.DoFn):
    def process(self, element):
        yield element.upper()

def run(input_path, output_path):
    # Define pipeline options
    options = PipelineOptions(
        runner='DataflowRunner',
        project='your-gcp-project-id',
        temp_location='gs://your-bucket/temp/',
        region='your-region'
    )

    # Create the pipeline
    with beam.Pipeline(options=options) as p:
        (
            p
            | 'Read from GCS' >> beam.io.ReadFromText(input_path)
            | 'Convert to Uppercase' >> beam.ParDo(UpperCaseTransform())
            | 'Write to GCS' >> beam.io.WriteToText(output_path)
        )

if __name__ == '__main__':
    input_path = 'gs://your-bucket/input/input.txt'
    output_path = 'gs://your-bucket/output/output.txt'
    run(input_path, output_path)
```

**Step 2:** Create a Dataflow Template from the Pipeline
To create a template, run the script with the following command, which generates a classic template and uploads it to the specified GCS path.
```bash
python my_pipeline.py \
  --runner=DataflowRunner \
  --project=your-gcp-project-id \
  --region=your-region \
  --temp_location=gs://your-bucket/temp/ \
  --staging_location=gs://your-bucket/staging/ \
  --template_location=gs://my-bucket/templates/my-template
```

* `template_location`: This is where the template file will be stored in GCS. In this example, it will be saved as gs://my-bucket/templates/my-template.
  * `temp_location` and `staging_location`: These are required to store temporary files during the template creation process.

**Step 3**: Running the Dataflow Job Using the Template
After creating the template, you can run a Dataflow job using the template from GCS with Terraform:
```bash
resource "google_dataflow_job" "my_dataflow_job" {
  name            = "example-dataflow-job"
  template_gcs_path = "gs://my-bucket/templates/my-template"
  parameters = {
    input_path  = "gs://your-bucket/input/input.txt"
    output_path = "gs://your-bucket/output/output.txt"
  }
  zone            = "us-central1-f"
}
```

## What Does the Template Contain?
The template itself does not contain the original Python code, but rather a packaged version of the pipeline, including:

* Information on the pipeline structure (e.g., the transformations and I/O operations).
* Metadata on how the pipeline should be executed (e.g., runner type, project settings).
* Any dependencies or libraries required for the execution (especially in the case of Flex Templates, where Docker containers may be used).

## Summary
* `template_gcs_path`: Refers to the location in GCS where a Dataflow template (compiled pipeline) is stored.
* `Dataflow Template`: A pre-packaged version of a pipeline created from Apache Beam code (Python or Java), used to run Dataflow jobs.
* `Example Flow`: 
    Write an Apache Beam pipeline → Create a Dataflow template by running the pipeline with template_location → Use the template to launch jobs via Terraform or the Dataflow console.

In this process, the Python code (`my_pipeline.py`) is the source from which the Dataflow template is generated. The resulting template is then used to execute the Dataflow job multiple times without having to rerun the original Python script.

# Concern-3
what does the below command do..? will it actually start and deploy the dataflow job or just create a package and places it at given gcs path
```bash
python my_pipeline.py \
  --runner=DataflowRunner \
  --project=your-gcp-project-id \
  --region=your-region \
  --temp_location=gs://your-bucket/temp/ \
  --staging_location=gs://your-bucket/staging/ \
  --template_location=gs://my-bucket/templates/my-template
```

The given command creates a Dataflow template and stores it in the specified Google Cloud Storage (GCS) location, but it does **not actually start or deploy a Dataflow job**. Here's what each part of the command does:

* `python my_pipeline.py`: Runs the Python script that defines the Apache Beam pipeline.
* `--runner=DataflowRunner`: Specifies that the pipeline should use the DataflowRunner, meaning that it is intended to be executed on Google Cloud Dataflow.
* `--project=your-gcp-project-id`: Indicates the Google Cloud project in which the Dataflow resources will be managed.
* `--region=your-region`: Specifies the region where the Dataflow job will run, such as us-central1 or europe-west1.
* `--temp_location=gs://your-bucket/temp/`: A GCS location where temporary files will be stored during the creation of the template.
* `--staging_location=gs://your-bucket/staging/`: A GCS location for staging files needed for the pipeline execution.
* `--template_location=gs://my-bucket/templates/my-template`: The location in GCS where the generated Dataflow template will be saved.

## What Does This Command Do?
This command compiles the Apache Beam pipeline code and creates a Dataflow template. The template is essentially a packaged version of the pipeline, which can later be used to deploy Dataflow jobs. It includes all necessary metadata, configurations, and dependencies required to execute the pipeline but **does not actually start the job itself**.

## Summary:
* Creates and uploads a Dataflow template to GCS (gs://my-bucket/templates/my-template).
* Does NOT deploy or start the Dataflow job.
* The generated template can be used later to start a Dataflow job using the template (either via Terraform, the Google Cloud Console, or the gcloud CLI).

# Concern-4
When using the terraform resource `"google_dataflow_job"` how to make sure it is for batch or streaming?

When using the `google_dataflow_job` Terraform resource, you can specify whether the Dataflow job is for `batch` or `streaming` processing by setting the appropriate pipeline options in the `template parameters or pipeline code`. 

There isn't a direct attribute in the Terraform resource to specify batch or streaming explicitly, but the type of job is determined by how the Apache Beam pipeline is configured.

## How to Set Up for Batch or Streaming
1. Configure the Pipeline for Batch or Streaming:
   * In the Apache Beam pipeline code, you determine if the job is batch or streaming based on the source used and how you configure the pipeline options.
  * Batch Processing: Typically reads from bounded data sources (e.g., files in Google Cloud Storage).
  * Streaming Processing: Typically reads from unbounded data sources (e.g., Google Cloud Pub/Sub).

2. Setting Up the Dataflow Job in Terraform:
You will pass parameters that align with either batch or streaming jobs. For instance, streaming jobs typically require configurations like a windowing strategy or a streaming read source.

Here's how to configure Terraform for both scenarios:

Batch Job Example:
```bash
resource "google_dataflow_job" "batch_job" {
  name             = "batch-dataflow-job"
  template_gcs_path = "gs://my-bucket/templates/my-batch-template"
  parameters = {
    input_path  = "gs://your-bucket/input/input.txt"
    output_path = "gs://your-bucket/output/output.txt"
  }
  zone             = "us-central1-f"
}
```

Streaming Job Example:
```bash
resource "google_dataflow_job" "streaming_job" {
  name             = "streaming-dataflow-job"
  template_gcs_path = "gs://my-bucket/templates/my-streaming-template"
  parameters = {
    input_topic  = "projects/your-gcp-project-id/topics/your-input-topic"
    output_path  = "gs://your-bucket/output/output.txt"
  }
  zone             = "us-central1-f"
}
```

3. Additional Configuration for Streaming Jobs:
* For streaming jobs, make sure the pipeline code is configured to handle unbounded data sources, such as reading from a Pub/Sub topic.
* You should also include options like enabling auto-scaling and setting a streaming engine for better performance.

## Summary
* The type of Dataflow job (batch or streaming) is primarily determined by the pipeline code and the data sources you use.
* In Terraform, you control whether the job is batch or streaming by providing the appropriate template and parameters.
* `Batch jobs` read from bounded sources, while `streaming jobs` read from unbounded sources such as Pub/Sub.

# Hands-On
Let's walk through creating a Google Cloud Dataflow template using a Python Apache Beam pipeline and uploading it to a Google Cloud Storage (GCS) bucket. We'll then use Terraform to create the Dataflow streaming job and all related resources, including the GCS bucket, Pub/Sub topic, and Dataflow job.

**Pre-requisite:**

1. Make sure you have Apache Beam package installed.
```bash
pip install apache-beam[gcp]

or 

pip install "apache-beam[gcp]"

or 

pip install apache-beam\[gcp\]

```
Incase your gets the error `The error zsh: no matches found: apache-beam[gcp]` occurs because in the zsh shell, square brackets are interpreted as special characters. To fix this, you can escape the square brackets or use quotes around the package name.

Either of these commands should work to install the `apache-beam[gcp]` package.

2. Make sure you are in right project.
```bash
gcloud config list

gcloud config set project gcphde-prim-dev-data

gcloud auth application-default set-quota-project gcphde-prim-dev-data
```

3. **Enable Dataflow API.**

4. **Make sure the User Account has right permission.**

* Step 1: Python Apache Beam Pipeline (Python Code)

    The Python code below defines a basic Apache Beam pipeline that reads lines from a Pub/Sub subscription, converts each line to uppercase, and writes the transformed output to a GCS bucket.

    Python Script [dataflow_pipeline.py](./Terraform_Dataflow/dataflow_pipeline.py)

* Step 2: Create a Dataflow Template
    
    To create the Dataflow template, run the following command. This will package the Python pipeline and create a template file that will be stored in a GCS bucket.

    The main goal of creating a template is to package the pipeline's transformation logic into a reusable format, so it can be used later with different inputs.

    To create a Dataflow template, you would typically run a command like this:
```bash
python3 dataflow_pipeline.py \
--runner=DataflowRunner \
--project=gcphde-prim-dev-data \
--region=us-central1 \
--temp_location=gs://dataflow-handson-mayank/temp/ \
--staging_location=gs://dataflow-handson-mayank/staging/ \
--template_location=gs://dataflow-handson-mayank/templates/uppercase-template \
--output_path=gs://dataflow-handson-mayank/output/
```
    When creating a Dataflow template, we typically do not include `input` or `output` parameters that would trigger a job.

    Ensure that your code in `dataflow_pipeline.py` checks for the presence of the `--template_location` argument and uses it to create a template instead of running a job. 

* Step 3: Terraform Configuration to Deploy Resources
  
    The following Terraform code will:

  * Create a GCS bucket for staging and template storage.
  * Create a Pub/Sub topic and subscription.
  * Use the Dataflow template to create a streaming Dataflow job.

    Terraform Code [main.tf]

  * Explanation:
    * Storage Bucket: Used to store temporary files and the Dataflow template.
    * Pub/Sub Topic and Subscription: For streaming data input.
    * Dataflow Job: Uses the template from GCS and runs the streaming job.
    * Parameters in google_dataflow_job: Pass the input subscription and output path to the template.

* Step 4: Deploying with Terraform
  * Initialize Terraform:
```bash
terraform init
```
  * Apply the Terraform configuration:
```bash
terraform apply
```

This will create all the resources, deploy the Dataflow job, and start the streaming pipeline that reads messages from the Pub/Sub subscription, converts them to uppercase, and writes the output to the GCS bucket.

## Summary
1. Python Code: Defines the Dataflow pipeline.
2. Template Creation: The command packages the pipeline into a GCS-stored template.
3. Terraform Setup: Manages GCS, Pub/Sub, and the Dataflow job deployment using the template.
   

# When to Use Windowing and why it is necessary?
In streaming pipelines, windowing is essential for operations like GroupByKey, Combine, or any other transform that requires grouping, as it divides the data into manageable chunks over time rather than trying to process the entire unbounded stream at once.

In streaming pipelines, windowing divides the unbounded data stream into manageable, bounded intervals. This allows operations like GroupByKey to work on a fixed set of data for each window, instead of attempting to group all data globally.

# Custom Template Creation
We can create dataflow jobs from the cloud console using google provided templates. For example, if we need to create a real time streaming job which reads data from pub/sub and write the data into a bigquery table we can select the pub/sub to Bigquery template while creating the dataflow job along with all required parameters. However, if we have different business use cases such as we have to read from multiple pubsubs topics/subs and write the data to multiple tables or if there are many transformation logic need to be implemented then we can create custom dataflow templates using Apache Beam. We can create an Apache Beam pipeline using java SDK or Python SDK.  Here, in this article we will see how the beam pipeline can be implemented using java SDK.

Let's say we have a requirement where we need to create a custom dataflow job which should read data from pubsub subscription and append the data to a bigquery table.

* input subscription: my_pubsub_test_subscription
* output table: my_bq_dataset.my_test_table

let's create the beam pipeline using java. you can download the code from repo.

# Question
I have created Pipeline in Python using Apache Beam SDK, and Dataflow jobs are running perfetcly from command-line.
Now i'd like to run those jobs from UI, for that I have to create template file for my job.
I found steps to create template in Java using Maven.
But how do i do it using the Python SDK?

## Solution
Templates are available for creation in the Dataflow Python SDK since April 2017.
[https://cloud.google.com/dataflow/docs/templates/creating-templates](https://cloud.google.com/dataflow/docs/guides/templates/creating-templates)

To run a template, no SDK is needed (which is the main problem templates try to solve), so you can run them from the UI, REST API, or CL and here is how https://cloud.google.com/dataflow/docs/guides/templates/running-templates  

# Reference
1. https://partly-cloudy.co.uk/2020/11/07/building-customizable-and-reusable-pipeline-using-dataflow-template/
2. https://www.dataengineertech.com/usecases/dataflow-custom-template-apache-beam
3. https://medium.com/cts-technologies/building-and-testing-dataflow-flex-templates-80ef6d1887c6 
4. https://medium.com/swlh/apache-beam-google-cloud-dataflow-and-creating-custom-templates-using-python-c666c151b4bc
5. Google already provides us with many examples of running the Dataflow jobs using python SDK and lots of examples can be found here : https://github.com/GoogleCloudPlatform/professional-services/tree/main/examples/dataflow-python-examples 
6. 
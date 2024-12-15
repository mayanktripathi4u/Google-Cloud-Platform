# Streaming Custom Template
To create a classic custom template in Dataflow that processes a Pub/Sub stream, transforms text, and validates fields before writing to BigQuery, follow these steps. This example will demonstrate:

1. Reading messages from a Pub/Sub subscription.
2. Applying transformations:
   * Converting the text to uppercase.
   * Changing the billing_status field values.
   * Validating the date field (within the last 30 days and not in the future).
   * Validating email format.
3. Writing the results to a BigQuery table.

## Folder Structure
Here’s an example of the folder structure:
```bash
template_streaming/
├── examples/
│   ├── __init__.py
│   └── mymodule.py
└── requirements.txt
```

## Step 1: Python Code (mymodule.py)
Create the mymodule.py file with the following [code](./examples/mymodule.py)

In this code, the command line argument parsing now supports ValueProvider, which is necessary for runtime parameter support. Parameters like input_subscription and output_table can be provided at runtime, making the Dataflow template reusable.

Note: Aas per the documentation, it says "To add runtime parameter support, modify the input file option to use ValueProvider. Replace add_argument with add_value_provider_argument." Explain this, and also modify the above code accordingly. 
Doc: https://cloud.google.com/dataflow/docs/guides/templates/creating-templates#use-valueprovider-in-your-pipeline-options

In Apache Beam, `ValueProvider` allows for runtime parameter support in Dataflow templates. When using `ValueProvider`, the parameter values are not hardcoded or statically defined in the pipeline, but instead, they can be provided at runtime. This makes it possible to customize the pipeline's behavior without modifying the code itself.

**Explanation of `ValueProvider`**

**Static Parameters**: Hardcoded parameters are set before the pipeline execution and remain constant. If the values need to change, the code has to be updated.

**Runtime Parameters with ValueProvider**: Using ValueProvider, parameters can be passed when the Dataflow job is launched from a template. This is especially useful when creating reusable templates where input parameters like file paths, Pub/Sub subscriptions, BigQuery tables, etc., need to be supplied dynamically.

To add runtime parameter support, we'll modify the existing code to:

* Replace `add_argument()` with `add_value_provider_argument()`, which allows parameters to be passed at runtime.
* Use `ValueProvider` objects for any parameters that may change at runtime.

## Step 2: Requirements File
Add the dependencies for Dataflow: [requirements.txt](requirements.txt)

## Step 3: Creating the Template
Use the following command to create the Dataflow template:
```bash
python -m examples.mymodule \
    --runner DataflowRunner \
    --project YOUR_PROJECT_ID \
    --region YOUR_REGION \
    --staging_location gs://YOUR_BUCKET_NAME/staging \
    --temp_location gs://YOUR_BUCKET_NAME/temp \
    --template_location gs://YOUR_BUCKET_NAME/templates/YOUR_TEMPLATE_NAME \
    --input_subscription projects/YOUR_PROJECT_ID/subscriptions/YOUR_SUBSCRIPTION_NAME \
    --output_table YOUR_PROJECT_ID:YOUR_DATASET.YOUR_TABLE
```

Replace `YOUR_PROJECT_ID`, `YOUR_REGION`, `YOUR_BUCKET_NAME`, `YOUR_SUBSCRIPTION_NAME`, `YOUR_DATASET`, and `YOUR_TABLE` with actual values.

```bash
python -m examples.mymodule \
    --runner DataflowRunner \
    --project gcphde-prim-dev-data \
    --region us-central1 \
    --staging_location gs://dataflow-handson-mayank/staging \
    --temp_location gs://dataflow-handson-mayank/temp \
    --template_location gs://dataflow-handson-mayank/templates/streaming_custom_template \
    --input_subscription projects/gcphde-prim-dev-data/subscriptions/my_streaming_pubsub_topic-sub \
    --requirements_file requirements.txt \
    --output_table gcphde-prim-dev-data:MyDataflowJob_ds.streaming_custom_processing
```

**Code Explanation**
* The script performs transformations on the incoming Pub/Sub data, including text conversion, status modification, date, and email validation.
* If all validations pass, the data is written to a specified BigQuery table.
* The template is created and saved in a specified GCS location, which can be used to launch Dataflow jobs later.

# Running classic templates
After you create and stage your Dataflow template, run the template with the Google Cloud console, REST API, or the Google Cloud CLI. You can deploy Dataflow template jobs from many environments, including App Engine standard environment, Cloud Run functions, and other constrained environments.

[Refer Google Doc](https://cloud.google.com/dataflow/docs/guides/templates/running-templates)

**Note:** 
When creating a Dataflow template, the `--input_subscription` parameter specifies a placeholder for a Pub/Sub subscription. You can still change the subscription when creating the actual Dataflow job using the template.

The key is that `ValueProvider` enables dynamic runtime parameterization. The value you provide for `--input_subscription` while creating the template acts as a default or placeholder. During the actual Dataflow job execution, you can override this parameter with a different subscription.

When launching a Dataflow job from this template, you can specify a **different subscription**.

To ensure the Dataflow job runs as a streaming job instead of a batch job, you need to configure the `PipelineOptions` for streaming when creating the Dataflow template. Specifically, you must set `StreamingOptions` by including `options.view_as(StandardOptions).streaming = True` in the Python code.

Example: Code Snippet
```bash
def run():
    # Define pipeline options
    pipeline_options = PipelineOptions()
    pipeline_options.view_as(StandardOptions).streaming = True
```

## Using GCloud
```bash
gcloud dataflow jobs run my_stream_dataflow_job \
    --gcs-location=gs://dataflow-handson-mayank/templates/streaming_custom_template \
    --region=us-central1 \
    --parameters input_subscription=projects/gcphde-prim-dev-data/subscriptions/streaming_pubsub_topic-sub
    
    # , output_path=gs://dataflow-handson-mayank/output/
```

```bash
gcloud dataflow jobs run my_batch_dataflow_job \
    --gcs-location=gs://dataflow-handson-mayank/templates/uppercase \
    --region=us-central1 
```

```bash
gcloud dataflow jobs run my_batch_dataflow_job \
    --gcs-location=gs://dataflow-handson-mayank/templates/uppercase \
    --region=us-central1 \
    --parameters input_subscription=projects/gcphde-prim-dev-data/subscriptions/streaming_pubsub_topic-sub, output_path=gs://dataflow-handson-mayank/output/
```

## Using Terraform

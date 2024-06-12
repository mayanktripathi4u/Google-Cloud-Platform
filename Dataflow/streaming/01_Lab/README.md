# Challenge to Self.
I am willing to create a streaming data pipeline, which will store the data into BQ using Pub/Sub topic and Dataflow.

Below are the steps I will be following -->
1. Create a cloud storage bucket as the temp location for dataflow jobs.
2. Create a BQ dataset and table to receive the streaming data.
3. create a pub/sub topic and test publishing messages to the topic.
4. create and run a dataflow job to stream data from pub/sub topic to BQ
5. run the query to valodate streaming data


Task 1: Create the Cloud Storage Bucket
        Bucket Name: mt_devops_bkt_01
        `gsutil mb gs://mt_devops_bkt_01`

Task 2: Create a BigQuery dataset and table
Create a BigQuery dataset called BigQuery dataset name in the region named US (multi region).In the created dataset, create a table called BigQuery table name.

    Project : proud-climber-421817
    Dataset : streamingDataSet
    Table : tbl_streamingData
    Schema : data STRING 

Task 3. Set up a Pub/Sub topic
Create a Pub/Sub topic called Pub/Sub topic name.Use the default settings, which has enabled the checkbox for Add a default subscription.
    Topic: projects/proud-climber-421817/topics/streamingPubSubTopic

Task 4. Run a Dataflow pipeline to stream data from a Pub/Sub topic to BigQuery
Create and run a Dataflow job called Dataflow job name to stream data from a Pub/Sub topic to the BigQuery table you created in a previous task.

Use the Pub/Sub topic that you created in a previous task: Pub/Sub topic name

Use the Cloud Storage bucket that you created in a previous task as the temporary location

Use the BigQuery dataset and table that you created in a previous task as the output table: BigQuery dataset name.BigQuery table name

Use Region as the regional endpoint.

GCloud Equivalent Command:
    gcloud dataflow jobs run <pubsub name> --gcs-location gs://dataflow-templates-us-east4/latest/PubSub_to_BigQuery --region us-east4 --staging-location gs://<temp bucket path> --additional-user-labels {} --parameters inputTopic=<topic id>, outputTableSpec=<BucBigQuery Full Path, note to add colon>

    gcloud dataflow jobs run streamingPubSubTopic --gcs-location gs://dataflow-templates-us-east4/latest/PubSub_to_BigQuery --region us-east4 --staging-location gs://mt_devops_bkt_01/temp/ --additional-user-labels {} --parameters inputTopic=projects/proud-climber-421817/topics/streamingPubSubTopic, outputTableSpec=proud-climber-421817:streamingDataSet.tbl_streamingData


    gcloud dataflow jobs run streamingPubSubTopic \
    --gcs-location gs://dataflow-templates-us-central1/latest/PubSub_to_BigQuery \
    --region us-central1 \
    --staging-location gs://mt_devops_bkt_01/temp/ \
    --parameters inputTopic=projects/proud-climber-421817/topics/streamingPubSubTopic,outputTableSpec=proud-climber-421817:streamingDataSet.tbl_streamingData

    [Refer to working code](/GCP/Dataflow/streaming/01_Lab/gcloud_command.txt)

Task 5. Publish a test message to the topic and validate data in BigQuery
Publish a message to your topic using the following code syntax for Message: `{"data": "Mayank is a Kind person"}`

Run a SELECT statement in BigQuery to see the test message populated in your table.

Note: If you do not see any test messages in your BigQuery table, check that the Dataflow job has a status of Running, and then send another test message.




Error:
Startup of the worker pool in zone us-central1-b failed to bring up any of the desired 1 workers. Please refer to https://cloud.google.com/dataflow/docs/guides/common-errors#worker-pool-failure for help troubleshooting. ZONE_RESOURCE_POOL_EXHAUSTED: Instance 'streamingpubsubtopic-05101229-kur0-harness-xcjb' creation failed: The zone 'projects/proud-climber-421817/zones/us-central1-b' does not have enough resources available to fulfill the request.  Try a different zone, or try again later.
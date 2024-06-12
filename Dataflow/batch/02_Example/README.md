1. Create below 3 files
    * demo.json
    * demo.js
    * data.csv

2. Create a Cloud Storage Bucket, and upload the above 3 files.
    * Bucket Name: dataflow_demo

3. Create a table in BigQuery, make sure 
    * Dataset: mySampleDataset
    * Table: customer

4. Create a Dataflow Job.
    * Create Job from Template
    * Job name: demojob
    * Regional endpoint: us-central1
    * Dataflow Template: Text Files on cloud storage to BigQuery
    * Required Parameters
        * JavaScript UDF Path in Cloud Storage: <provide the storage bucket path of demo.js example: gs://myBucket/demo.js> 
        * JavaScript UDF name: <name of the funtion from your demo.js, which is transform>
        * BigQuery Output Table: project123:mySampleDataset.customer
        * Cloud Storage input path: <provide the storage bucket path of data.csv example: gs://myBucket/data.csv> 
        * Temporary BigQuery Directory: gs://myBucket/temp_bq
        * Temporary location: gs://myBucket/temp
        * Optional Parameters
            * Max Workers: 1
            * Number of workers: 1
        * Run Job (click button)
    
    
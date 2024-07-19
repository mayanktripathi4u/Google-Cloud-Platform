# Ways to Load data into BigQuery

load_table_from_uri
load_table_from_file
LoadJobConfig


# Upload the CSV file into existing BQ Table
1. Create Project; Dataset; and Table. Load some data into table as initial load.
2. Create a CSV file with New records. This file data will get append to existing data in table.
3. Activate Cloud Shell
4. Check the working Project in the Shell.
5. Use Code to update table.
    ```
    bq load myDataset.testTable gs://mybucket/samplefile.csv
    ```
    Or
    ```
    LOAD DATA OVERWRITE myDataset.myTable (col1, col2,..)
    FROM FILES (
        FORMAT='CSV'
        URIS=['gs://bucket_path/myfile.csv']
    );
    ```
6. Validate.

# References
1. Google Docs https://cloud.google.com/bigquery/docs/loading-data 
2. 
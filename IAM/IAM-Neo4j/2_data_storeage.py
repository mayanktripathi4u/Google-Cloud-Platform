from google.cloud import bigquery

def store_iam_data(iam_data):
    client = bigquery.Client()
    table_id = "your-project.iam_dataset.iam_table"

    # Convert IAM data to appropriate format for BigQuery
    rows_to_insert = [
        {"project_id": data["project"], "policy": str(data["policy"])}
        for data in iam_data
    ]

    errors = client.insert_rows_json(table_id, rows_to_insert)
    if errors == []:
        print("IAM data loaded into BigQuery successfully.")
    else:
        print(f"Errors occurred: {errors}")

store_iam_data(iam_data)
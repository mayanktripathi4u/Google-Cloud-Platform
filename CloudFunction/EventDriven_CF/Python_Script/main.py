import pandas as pd
import pdfplumber
from tempfile import NamedTemporaryFile
from google.cloud import storage

def pdf_to_excel(event, context):
    # Get the Bucket and PDF file name from the CLoud Storage Event
    dest_bucket_name = 'demo-dest-bkt-21july'
    print("Strating cloud function execution....")
    bucket_name = event["bucket"]
    file_name = event["name"]
    print("Bucket Name : ", bucket_name)
    print("FILE Name : ", file_name)

    # Initialize Google Cloud Storage Client
    client = storage.Client()

    # Get the bucket containing the PDF file
    bucket = client.get_bucket(bucket_name)
    dest_bucket =client.get_bucket(dest_bucket_name)

    # Download the PDF file to a temp loc.
    temp_df_file = NamedTemporaryFile(delete=False)
    blob = bucket.blob(file_name)
    blob.download_to_filename(temp_df_file.name)

    # Extract tables from the PDF
    with pdfplumber.open(temp_df_file) as pdf:
        tables = []
        for page in pdf.pages:
            table = page.extract_table()
            if table:
                tables.extend(table)

    # Convert tables to Data Frame
    df = pd.DataFrame(tables)

    # Write DataFrame to Excel
    excel_output = NamedTemporaryFile(suffix='.xlsx', delete=False)
    df.to_excel(excel_output.name, index=False)

    # Upload excel file to Cloud storage
    execl_blob = dest_bucket.blob(f"{file_name}.xlsx")
    execl_blob.upload_from_filename(excel_output.name)

    # Delete Temp File
    temp_df_file.close()
    excel_output.close()

    print(f"Converted PDF to Excel : {file_name}.xlsx")

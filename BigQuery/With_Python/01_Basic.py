import os
from google.cloud import bigquery

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'proud-climber-421817-14ec0fc568ac.json'

client = bigquery.Client()

sql_query = """
SELECT * FROM `proud-climber-421817.streamingDataSet.tbl_streamingData`
LIMIT 10
"""

query_job = client.query(sql_query)

print(query_job)

print(query_job.result())

for row in query_job.result():
    print(row)
    


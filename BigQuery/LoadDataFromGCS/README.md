# Loading data into BigQuery from Cloud Stirage Bucket with Python

![alt text](image.png)

# Flow
pip install google.cloud.bigquery
pip install google.cloud.storage

1. main.py
2. schema.yaml
3. test_data.json
4. event.py
5. test.py  --> to test

# Test from Local / Workstation (not on cloud)

python3 -m venv .bqenv
source .bqenv/bin/activate
pip install google.cloud.bigquery google.cloud.storage
pip install pyyaml
python3 test.py

deactivate

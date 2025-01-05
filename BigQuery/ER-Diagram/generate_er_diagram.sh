#!/bin/bash

# Set Google Cloud Project ID
export GOOGLE_CLOUD_PROJECT="gcphde-prim-dev-data"

# Run the Python script to generate the ER diagram
python3 extract_generate_erd.py

# Optionally, you could move the generated .drawio file to the appropriate folder
# mv er_diagram.drawio /Users/tripathimachine/Desktop/Apps/GitHub_Repo/Google-Cloud-Platform/BigQuery/ER-Diagram/

echo "ER diagram generation complete."

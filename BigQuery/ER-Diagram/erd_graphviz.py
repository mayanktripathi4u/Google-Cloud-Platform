"""
Graphviz is a powerful tool for generating diagrams programmatically using the DOT language. You can create a graph representation of your BigQuery schema and generate an ER diagram directly in Python.

Steps:
1. Extract BigQuery schema using Python.
2. Convert schema to Graphviz DOT format.
3. Generate ER diagram image (PNG/SVG) using Graphviz.

Install Packages:
    pip install graphviz google-cloud-bigquery

On macOS: brew install graphviz
"""

# Import
from google.cloud import bigquery
from graphviz import Source

# 1. Extract BigQuery schema using Python.

def get_bigquery_schema(project_id, dataset_id):
    client = bigquery.Client(project=project_id)
    
    # Fetch dataset
    dataset_ref = client.dataset(dataset_id)
    tables = client.list_tables(dataset_ref)
    
    schema_info = {}
    
    # Loop through tables and fetch columns
    for table in tables:
        table_ref = client.get_table(table)
        columns = [field.name for field in table_ref.schema]
        schema_info[table.table_id] = columns
    
    return schema_info

# 2. Convert BigQuery Schema to Graphviz DOT Format
def convert_schema_to_dot(schema_info):
    dot_content = "digraph G {\n"
    
    # Loop through schema to create nodes for each table
    for table, columns in schema_info.items():
        node_id = table.replace(" ", "_").replace("-", "_")  # Clean table name
        dot_content += f'  "{node_id}" [label="{table}\\n' + "\\n".join(columns) + '"];\n'
    
    # Generate relationships (if needed)
    for table, columns in schema_info.items():
        if "id" in columns:  # Example: Link tables by 'id' column
            dot_content += f'  "{table}" -> "another_table" [label="id"];\n'
    
    dot_content += "}\n"
    return dot_content

# Generate the ER Diagram
# from graphviz import Source

# Define project and dataset

project_id = 'gcphde-prim-dev-data'
dataset_id = 'sample_dataset'

# Get schema info
schema_info = get_bigquery_schema(project_id, dataset_id)

# Convert schema to DOT format
dot_file_content = convert_schema_to_dot(schema_info)

# Generate Graphviz source
source = Source(dot_file_content)

# Render as PNG or SVG
source.render("er_diagram_graphviz", format="png", cleanup=True)  # or format="svg"



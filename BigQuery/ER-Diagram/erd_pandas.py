"""
Use Pandas and NetworkX for graph-based representations and Matplotlib for visualizing the graph.

Steps:
1. Extract schema from BigQuery.
2. Create relationships and represent them as a graph.
3. Visualize the graph with NetworkX and Matplotlib.

Install Packages:
    pip install google-cloud-bigquery networkx matplotlib pandas

    
"""

# Import
from google.cloud import bigquery
import matplotlib.pyplot as plt
import networkx as nx

# 1. Extract BigQuery Schema


def get_bigquery_schema(project_id, dataset_id):
    client = bigquery.Client(project=project_id)
    
    # Fetch dataset and tables
    dataset_ref = client.dataset(dataset_id)
    tables = client.list_tables(dataset_ref)
    
    schema_info = {}
    
    # Loop through tables and fetch columns
    for table in tables:
        table_ref = client.get_table(table)
        columns = [field.name for field in table_ref.schema]
        schema_info[table.table_id] = columns
    
    return schema_info

# 2. Generate ER Diagram with NetworkX and Matplotlib
def visualize_er_diagram(schema_info):
    # Create a directed graph
    G = nx.DiGraph()

    # Add nodes for each table
    for table, columns in schema_info.items():
        G.add_node(table, label=', '.join(columns))

    # Define relationships (for simplicity, assume tables are linked by 'id')
    for table, columns in schema_info.items():
        if "id" in columns:
            G.add_edge(table, "another_table")  # Example edge, replace with actual logic

    # Create a layout and draw the graph
    pos = nx.spring_layout(G, seed=42)  # Layout algorithm
    labels = nx.get_node_attributes(G, 'label')
    
    # Draw the graph with labels
    nx.draw(G, pos, with_labels=True, node_size=3000, node_color="skyblue", font_size=10, font_weight='bold')
    nx.draw_networkx_labels(G, pos, labels, font_size=8)
    
    # Display the plot
    plt.show()

# Define project and dataset
project_id = 'gcphde-prim-dev-data'
dataset_id = 'sample_dataset'

# Get schema info
schema_info = get_bigquery_schema(project_id, dataset_id)

# Visualize ER diagram
visualize_er_diagram(schema_info)

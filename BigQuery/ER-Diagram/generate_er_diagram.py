import pydot
from google.cloud import bigquery

# Function to generate ER Diagram in DOT format
def create_er_diagram(schemas):
    print("........... create_er_diagram is called ...........")
    graph = pydot.Dot(graph_type='digraph')

    # Create nodes for each table
    for table, columns in schemas.items():
        print(f"Creating Node for {table} --> {columns}")
        node = pydot.Node(table, shape='record', label='{ ' + ' | '.join(columns) + ' }')
        graph.add_node(node)

    # Optionally, you could add edges to represent relationships between tables (foreign keys, etc.)
    # For now, we will just create nodes for tables without relationships.
    
    return graph


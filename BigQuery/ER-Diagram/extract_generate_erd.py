from google.cloud import bigquery
import pydot

print(f"extract table schema process initiated!")

# Initialize the BigQuery client
client = bigquery.Client()

def get_bigquery_schema(project_id, dataset_id):
    print(f".......get_bigquery_schema function called.......")
    dataset_ref = client.dataset(dataset_id, project=project_id)
    tables = client.list_tables(dataset_ref)  # List all tables in the dataset
    table_schemas = {}

    for table in tables:
        print(f"Running loop for table: {table}, to fetch schema.")
        table_ref = dataset_ref.table(table.table_id)
        schema = client.get_table(table_ref).schema  # Get the schema for each table
        table_schemas[table.table_id] = [field.name for field in schema]  # Store column names

    return table_schemas


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

def create_drawio_xml(schemas):
    print("......... create_drawio_xml ...........")

    # Start the XML structure
    # <mxGraphModel dx="840" dy="631" grid="1" gridSize="10" guides="1">
    xml = """<?xml version="1.0" encoding="UTF-8"?>
    <mxfile>
      <diagram name="BQ-ER-Diagram">
        <mxGraphModel dx="840" dy="631" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="2000" pageHeight="2000" math="0" shadow="0">
          <root>
            <mxCell id="0" />
            <mxCell id="1" parent="0" />
    """

    # # Create nodes for each table
    # for table, columns in schemas.items():
    #     node_label = f"<mxCell value='{table} | {', '.join(columns)}' style='rounded=1;whiteSpace=wrap;html=1;' vertex='1' connectable='0' parent='1' />"
    #     xml += node_label

    # Create nodes for each table and their columns (Create nodes for each table with x, y position)
    table_counter = 2  # Start ID counter for mxCell nodes
    x_pos, y_pos = 200, 200  # Initial position for the first table
    table_positions = {}  # Dictionary to store positions

    for table, columns in schemas.items():
        node_id = table_counter
        node_label = f"<mxCell id='{node_id}' value='{table}\\n{', '.join(columns)}' style='rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;' vertex='1' connectable='0' parent='1' x='{x_pos}' y='{y_pos}' />"
        # node_label = f"<mxCell id='{node_id}' value='{table}\\n{', '.join(columns)}' style='rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;' vertex='1' connectable='0' parent='1' />"
        xml += node_label

        table_positions[table] = (x_pos, y_pos)  # Store the position for this table
        
        # Increment the position for the next table (spread them out)
        x_pos += 300  # Move next table 200px to the right
        if x_pos > 1500:  # If it exceeds 600px, move down and reset x
            x_pos = 200
            y_pos += 300  # Move down 200px to create a new row of tables

        table_counter += 1

    # Close the XML structure
    xml += """
          </root>
        </mxGraphModel>
      </diagram>
    </mxfile>"""

    print(f"XML generated is {xml}")

    # Save XML file for draw.io
    print(f"Starting to create er_diagram.drawio file")
    with open("er_diagram.drawio", "w") as f:
        f.write(xml)

    print("er_diagram.drawio file is created and schema is converted to XML format.")


# Starting point............
project_id = 'gcphde-prim-dev-data'
dataset_id = 'sample_dataset'
schemas = get_bigquery_schema(project_id, dataset_id)

# Print the schema of all tables
for table_name, columns in schemas.items():
    print(f"Table: {table_name}")
    for column in columns:
        print(f"  - {column}")


# Create ER diagram
er_graph = create_er_diagram(schemas)

print(f"...... er_graph is populated ...... {er_graph}")

# Output ER diagram to a PNG file
er_graph.write_png('er_diagram.png')

# Optionally, you can also save the DOT file for later use or visualization
er_graph.write_dot('er_diagram.dot')

# Convert to XML
create_drawio_xml(schemas)
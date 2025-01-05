def create_drawio_xml(schemas):
    # Start the XML structure
    xml = """<?xml version="1.0" encoding="UTF-8"?>
    <mxfile>
      <diagram name="Sample ER Diagram-2">
        <mxGraphModel dx="0" dy="0" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="5000" pageHeight="5000" math="0" shadow="0">
          <root>
            <mxCell id="0" />
            <mxCell id="1" parent="0" />
    """
    
    # Initialize starting coordinates (positive coordinates inside canvas)
    x_pos, y_pos = 100, 100  # Start at the top-left corner (positive coordinates)
    table_counter = 2  # ID for first table node
    max_x_pos = 4500  # Max X position before wrapping to next row
    horizontal_spacing = 400  # Horizontal spacing between tables
    vertical_spacing = 400  # Vertical spacing between rows

    # Create nodes for each table with correct x, y positions
    for table, columns in schemas.items():
        node_id = table_counter
        node_label = f"<mxCell id='{node_id}' value='{table}\\n{', '.join(columns)}' style='rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;' vertex='1' connectable='0' parent='1' x='{x_pos}' y='{y_pos}' />"
        xml += node_label
        
        # Update the x and y positions for the next table
        x_pos += horizontal_spacing  # Move next table to the right
        
        if x_pos > max_x_pos:  # If we exceed max x-coordinate, move to the next row
            x_pos = 100  # Reset x position
            y_pos += vertical_spacing  # Move y position down

        table_counter += 1  # Increment the table counter

    # Close the XML structure for the diagram
    xml += """
          </root>
        </mxGraphModel>
      </diagram>
    </mxfile>
    """

    # Save the generated XML to a .drawio file
    with open("er_diagram.drawio", "w") as f:
        f.write(xml)

# Sample schema of tables
schemas = {
    "table_1": ["col1", "col2", "col3"],
    "table_2": ["col1", "col2"],
    "table_3": ["col1", "col2", "col3"],
    "table_4": ["col1", "col2", "col3", "col4"],
    "table_5": ["col1", "col2"],
    "table_6": ["col1", "col2", "col3", "col4"],
    "table_7": ["col1", "col2"],
}

create_drawio_xml(schemas)

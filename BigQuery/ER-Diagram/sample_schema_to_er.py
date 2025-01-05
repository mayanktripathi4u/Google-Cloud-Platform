def create_drawio_xml(schemas):
    # Start the XML structure
    xml = """<?xml version="1.0" encoding="UTF-8"?>
    <mxfile>
      <diagram name="Sample ER Diagram">
        <mxGraphModel dx="840" dy="631" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="0.5" pageWidth="2000" pageHeight="2000" math="0" shadow="0">
          <root>
            <mxCell id="0" />
            <mxCell id="1" parent="0" />
    """

    # Initial positions for the first table
    x_pos, y_pos = 200, 200  # Starting coordinates within visible area
    table_counter = 2  # Start ID counter for mxCell nodes

    # Create nodes for each table with x, y position
    for table, columns in schemas.items():
        node_id = table_counter
        node_label = f"<mxCell id='{node_id}' value='{table}\\n{', '.join(columns)}' style='rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;' vertex='1' connectable='0' parent='1' x='{x_pos}' y='{y_pos}' />"
        xml += node_label
        
        # Increment positions for next table
        x_pos += 300  # Move the next table 300px to the right
        if x_pos > 1500:  # If x exceeds 1500, move to a new row (y coordinate)
            x_pos = 200  # Reset x position
            y_pos += 300  # Move down by 300px for the next row

        table_counter += 1

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

    print(f"XML Output : {xml}")

# Testing
schemas = {
    "table_1": ["col1", "col2", "col3"],
    "table_2": ["col1", "col2"],
    "table_3": ["col1", "col2", "col3"],
    "table_4": ["col1", "col2", "col3", "col4"],
    # Add more tables if needed
}
create_drawio_xml(schemas)




'''
You can explicitly set the pageScale to 1 or even adjust it to 0.5 or 2 to control the zoom level of the diagram. This might help to make the diagram appear at the right size.
The scale of 0.5 will zoom out the diagram, while 2 would zoom it in. You can experiment with these values.

canvas size of 2000 x 2000
'''
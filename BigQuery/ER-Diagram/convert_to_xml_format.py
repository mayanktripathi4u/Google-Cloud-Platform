def create_drawio_xml(schemas):
    # Start the XML structure
    xml = """<?xml version="1.0" encoding="UTF-8"?>
    <mxfile>
      <diagram name="Page-1">
        <mxGraphModel dx="840" dy="631" grid="1" gridSize="10" guides="1">
          <root>
            <mxCell id="0" />
            <mxCell id="1" parent="0" />
    """

    # Create nodes for each table
    for table, columns in schemas.items():
        node_label = f"<mxCell value='{table} | {', '.join(columns)}' style='rounded=1;whiteSpace=wrap;html=1;' vertex='1' connectable='0' parent='1' />"
        xml += node_label

    # Close the XML structure
    xml += """
          </root>
        </mxGraphModel>
      </diagram>
    </mxfile>"""

    # Save XML file for draw.io
    with open("er_diagram.drawio", "w") as f:
        f.write(xml)

# Call the Function
create_drawio_xml(schemas)

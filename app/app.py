# Import the required modules
import csv
import xml.etree.ElementTree as ET

# Define the reqif namespace and prefix
reqif_ns = "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"
ET.register_namespace("reqif", reqif_ns)
reqif_prefix = "{%s}" % reqif_ns

# Create the root element of the reqif document
reqif_root = ET.Element(reqif_prefix + "REQ-IF")

# Create the core content element and append it to the root
core_content = ET.SubElement(reqif_root, reqif_prefix + "CORE-CONTENT")

# Create the requirements element and append it to the core content
requirements = ET.SubElement(core_content, reqif_prefix + "REQUIREMENTS")

# Create the spec objects element and append it to the requirements
spec_objects = ET.SubElement(requirements, reqif_prefix + "SPEC-OBJECTS")

# Open the csv file and read it as a dictionary
with open("data.csv", mode="r") as csv_file:
    csv_reader = csv.DictReader(csv_file)

    # Loop through each row in the csv file
    for row in csv_reader:

        # Create a spec object element and append it to the spec objects
        spec_object = ET.SubElement(spec_objects, reqif_prefix + "SPEC-OBJECT")

        # Set the identifier attribute of the spec object
        spec_object.set("IDENTIFIER", row["ID"])

        # Set the type attribute of the spec object
        spec_object.set("TYPE", row["SpecType"])

        # Create a values element and append it to the spec object
        values = ET.SubElement(spec_object, reqif_prefix + "VALUES")

        # Create a attribute value xhtml element and append it to the values
        attribute_value_xhtml = ET.SubElement(values, reqif_prefix + "ATTRIBUTE-VALUE-XHTML")

        # Set the definition attribute of the attribute value xhtml
        attribute_value_xhtml.set("DEFINITION", row["Type"])

        # Create a value element and append it to the attribute value xhtml
        value = ET.SubElement(attribute_value_xhtml, reqif_prefix + "THE-VALUE")

        # Set the text content of the value element to the text column of the csv row
        value.text = row["Text"]

# Create an ElementTree object from the root element
reqif_tree = ET.ElementTree(reqif_root)

# Write the ElementTree object to a reqif file with pretty printing
reqif_tree.write("example.reqif", encoding="utf-8", xml_declaration=True, method="xml")
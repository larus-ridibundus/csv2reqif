import csv
from lxml import etree

# Define the column names in the CSV file
csv_columns = ['ID', 'Name', 'Description']

# Define the ReqIF namespace and prefix
reqif_uri = "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"
reqif_prefix = "reqif"

# Create the root element of the ReqIF file
root = etree.Element("{" + reqif_uri + "}ReqIF", nsmap={reqif_prefix: reqif_uri})

# Create the header element and add it to the root
header = etree.Element("{" + reqif_uri + "}TheHeader", attrib={
    "version": "1.0",
    "comment": "ReqIF file generated from CSV data"
})
root.append(header)

# Create the core content element and add it to the root
core_content = etree.Element("{" + reqif_uri + "}CoreContent")
root.append(core_content)

# Read data from the CSV file and add it to the ReqIF file
with open('data.csv', 'r') as csv_file:
    print("open('data.csv', 'r')")
    reader = csv.DictReader(csv_file, fieldnames=csv_columns)
    for row in reader:
        requirement = etree.Element("{" + reqif_uri + "}Requirement", attrib={
            "IDENTIFIER": row['ID']
        })

        name = etree.Element("{" + reqif_uri + "}Name")
        name.text = row['Name']
        requirement.append(name)

        description = etree.Element("{" + reqif_uri + "}Description")
        description.text = row['Description']
        requirement.append(description)

        core_content.append(requirement)

# Write the ReqIF file to disk
with open('output.reqif', 'wb') as reqif_file:
    reqif_file.write(etree.tostring(root, pretty_print=True))
    print(reqif_file)
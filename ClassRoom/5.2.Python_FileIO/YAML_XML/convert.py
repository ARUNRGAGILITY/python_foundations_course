import xml.etree.ElementTree as ET
import yaml

def prettify(element, indent='  ', level=0):
    """Recursively add indentation and line breaks to make the XML output readable."""
    if element:  # if the element has children
        if not element.text or not element.text.strip():
            element.text = "\n" + indent * (level+1)
        if not element.tail or not element.tail.strip():
            element.tail = "\n" + indent * level
        for element in element:
            prettify(element, indent, level+1)
    else:  # if the element is empty
        if level and (not element.tail or not element.tail.strip()):
            element.tail = "\n" + indent * level
    if not level:
        element.tail = "\n"

def add_elements(parent, elements):
    for element in elements:
        el = ET.SubElement(parent, element['element'])
        for attr, value in element.get('attributes', {}).items():
            el.set(attr, value)
        if 'text' in element:
            el.text = element['text']
        if 'children' in element:
            add_elements(el, element['children'])

# Assuming the YAML file ('config.yaml') is already created and loaded into 'config'
with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)

# Create the root element
root_element = list(config.keys())[0]
root = ET.Element(root_element)

# Add elements from the YAML configuration
add_elements(root, config[root_element])

# Prettify the XML output
prettify(root)

# Create the ElementTree and write to an XML file with indentation
tree = ET.ElementTree(root)
tree.write('output.xml', encoding='utf-8', xml_declaration=True)

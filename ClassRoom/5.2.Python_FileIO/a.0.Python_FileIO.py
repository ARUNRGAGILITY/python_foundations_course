import csv
import json
import pandas as pd
import xml.etree.ElementTree as ET
import yaml
import configparser

# Text File
# Writing to a text file
with open('example.txt', 'w') as file:
    file.write('Hello, world!')
# Appending text to the same file
with open('example.txt', 'a') as file:
    file.write('\nThis is an appended line!')
# Reading from the text file
with open('example.txt', 'r') as file:
    print(file.read())


# CSV File
with open('example.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Age'])
    writer.writerow(['Alice', 24])
    writer.writerow(['Bob', 19])
with open('example.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# Excel File
df = pd.DataFrame({'Name': ['Alice', 'Bob'], 'Age': [24, 19]})
df.to_excel('example.xlsx', index=False)
print(pd.read_excel('example.xlsx'))

# JSON File
with open('example.json', 'w') as file:
    json.dump({'name': 'Alice', 'age': 24}, file)
with open('example.json', 'r') as file:
    print(json.load(file))

# XML File
data = ET.Element('data')
items = ET.SubElement(data, 'items')
item1 = ET.SubElement(items, 'item')
item1.set('name', 'item1')
tree = ET.ElementTree(data)
tree.write('example.xml')
tree = ET.parse('example.xml')
root = tree.getroot()
for child in root:
    print(child.tag, child.attrib)

# YAML File
with open('example.yaml', 'w') as file:
    yaml.dump({'name': 'Alice', 'age': 24}, file)
with open('example.yaml', 'r') as file:
    print(yaml.safe_load(file))


'''
YAML - Yet another markup language
# An example of a YAML file
user:
  name: John Doe
  age: 30
  married: true
  hobbies:
    - Reading
    - Photography
    - Programming
address:
  street: 123 Main St
  city: Anytown
  zip: 12345
  
user and address are keys that map to nested structures.
Indentation (spaces, not tabs) is used to represent structure.
Lists are denoted by hyphens.
It includes a comment (line starting with #), which is ignored by the parser.
'''
import yaml

# Writing data to a YAML file
data_to_write = {
    'user1': {'name': 'Alice', 'age': 30, 'city': 'New York'},
    'user2': {'name': 'Bob', 'age': 25, 'city': 'London'}
}
with open('example.yaml', 'w') as file:
    yaml.dump(data_to_write, file)

# Reading data from the YAML file
with open('example.yaml', 'r') as file:
    data_read = yaml.safe_load(file)
print("Original Data:")
print(data_read)

# Appending new data to the YAML file
data_to_append = {'user3': {'name': 'Charlie', 'age': 35, 'city': 'Paris'}}
with open('example.yaml', 'a') as file:
    yaml.dump(data_to_append, file, default_flow_style=False)

# Reading the appended data
with open('example.yaml', 'r') as file:
    data_appended = yaml.safe_load(file)
print("\nData After Appending:")
print(data_appended)

# Modifying an existing entry and writing back to the file
data_appended['user1']['age'] = 31  # Modifying Alice's age
with open('example.yaml', 'w') as file:
    yaml.dump(data_appended, file)

# Reading the modified data
with open('example.yaml', 'r') as file:
    data_modified = yaml.safe_load(file)
print("\nData After Modification:")
print(data_modified)


# INI File
config = configparser.ConfigParser()
config['DEFAULT'] = {'ServerAliveInterval': '45',
                     'Compression': 'yes',
                     'CompressionLevel': '9'}
config['bitbucket.org'] = {}
config['bitbucket.org']['User'] = 'hg'
with open('example.ini', 'w') as configfile:
    config.write(configfile)
config.read('example.ini')
for section in config.sections():
    print(f"Section: {section}")
    for key in config[section]:
        print(f"{key} = {config[section][key]}")


# Example: INI file
'''
[general]
app_name = ExampleApp
version = 1.0

[user_settings]
username = user123
email = user123@example.com
theme = dark

[server]
host = localhost
port = 8080

'''
import configparser

# Create a new INI file
config = configparser.ConfigParser()

config['general'] = {
    'app_name': 'ExampleApp',
    'version': '1.0'
}
config['user_settings'] = {
    'username': 'user123',
    'email': 'user123@example.com',
    'theme': 'dark'
}
config['server'] = {
    'host': 'localhost',
    'port': '8080'
}

# Write to the file (Create)
with open('example.ini', 'w') as configfile:
    config.write(configfile)

# Read from the file
config.read('example.ini')

# Read operations (Read)
app_name = config['general']['app_name']
print(f"App Name: {app_name}")

# Update the file (Update)
config['user_settings']['theme'] = 'light'

# Delete a setting (Delete)
del config['server']['port']

# Write these changes back to the file
with open('example.ini', 'w') as configfile:
    config.write(configfile)

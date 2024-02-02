# Dictionary Operations in Python

# Initialization
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

# Accessing Values
name = my_dict['name']
age = my_dict['age']

# Adding a New Key-Value Pair
my_dict['country'] = 'USA'

# Modifying an Existing Key's Value
my_dict['age'] = 31

# Removing an Item by Key
del my_dict['city']

# Checking Existence
if 'name' in my_dict:
    print("Name exists in the dictionary")

# Getting Keys and Values
keys = list(my_dict.keys())
values = list(my_dict.values())

# Iterating Through a Dictionary
for key in my_dict:
    print(key, my_dict[key])

# Creating a New Dictionary using Dictionary Comprehension
squared_dict = {x: x**2 for x in range(1, 6)}

# Copying a Dictionary (Shallow Copy)
copy_dict = my_dict.copy()

# Creating a New Dictionary by Unpacking
new_dict = {**my_dict}

# Clearing a Dictionary
my_dict.clear()

# Output
print("Name:", name)
print("Age:", age)
print("Updated Dictionary:", my_dict)
print("Keys:", keys)
print("Values:", values)
print("Squared Dictionary:", squared_dict)


# Combining Dictionaries by Unpacking

# Define two dictionaries
dict1 = {'name': 'John', 'age': 30}
dict2 = {'city': 'New York', 'country': 'USA'}

# Combine dictionaries using unpacking
combined_dict = {**dict1, **dict2}

# Output
print("Combined Dictionary:", combined_dict)

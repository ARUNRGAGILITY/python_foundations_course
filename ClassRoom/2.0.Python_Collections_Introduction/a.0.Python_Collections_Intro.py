# Python Collections Introduction

# Python Collections: Basics are List, Tuple, Set and Dictionary

# List is a ordered, mutable, duplicates allowed, sequential data type []
# Tuple is a ordered, immutable, duplicates allowed, sequential data type ()
# Set is a ordered, mutable, duplicates NOT allowed, sequential data type {}
# Dictionary is an unordered, mutable, duplicates NOT allowed, mapping data type {}

list_example = [1, 10, 40, True, False, "John", 20.34, 3+4j]
print(list_example)

tuple_example = (111, 120, 2200, "new data", True, False, "Ajax", 20.34, 3+4j)
print(tuple_example)

set_example = {10,20,30,40,70,90}
print(set_example)

dictionary_example = {'name': "John", 'occupation': "Engineer", 'age':40, 'bank_balance': 12121313.32}
print(dictionary_example)

# List, Tuple, Set Operations

# Comparison of Common Operations in List, Tuple, and Set

"""
| Operation              | List         | Tuple              | Set                    |
|------------------------|--------------|--------------------|------------------------|
| Initialization         | lst = [1, 2, 3] | tup = (1, 2, 3) | st = {1, 2, 3}         |
| Add an element         | lst.append(4)   | Not supported   | st.add(4)              |
| Remove an element      | lst.remove(2)   | Not supported   | st.remove(2)           |
| Access by index        | lst[0]          | tup[0]          | Not supported          |
| Check existence        | 2 in lst        | 2 in tup        | 2 in st                |
| Length                 | len(lst)        | len(tup)        | len(st)                |
| Concatenation          | lst1 + lst2     | tup1 + tup2     | Not directly supported |
| Iterate                | for x in lst:   | for x in tup:   | for x in st:           |
| Mutable (Changeable)   | Yes              | No             | Yes                    |
| Duplicates Allowed     | Yes              | Yes            | No                     |
| Order Preserved        | Yes              | Yes            | No                     |
"""

# Note: This comment block provides a quick reference for understanding the capabilities and limitations
# of lists, tuples, and sets in Python.

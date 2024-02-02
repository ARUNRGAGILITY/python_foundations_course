# Set Operations in Python

# 1. Initialization
my_set = {1, 2, 3, 4}

# 2. Adding Elements
my_set.add(5)  # Add a single element
my_set.update([6, 7])  # Add multiple elements

# 3. Removing Elements
my_set.remove(2)  # Remove a specific element (raises KeyError if not found)
my_set.discard(3)  # Remove a specific element (does not raise KeyError if not found)
element = my_set.pop()  # Remove and return an arbitrary element

# 4. Length of Set
# To find out how many elements are in the set
length = len(my_set)

# 5. Looping Through Set
# Sets can be iterated through just like lists
for item in my_set:
    print(item)

# 6. Checking Existence
# Check if an element exists within the set
if 1 in my_set:
    print("1 is in the set")

# 7. Set Operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Union
union_set = set1.union(set2)  # {1, 2, 3, 4, 5}

# Intersection
intersection_set = set1.intersection(set2)  # {3}

# Difference
difference_set = set1.difference(set2)  # {1, 2}

# Symmetric Difference
symmetric_difference_set = set1.symmetric_difference(set2)  # {1, 2, 4, 5}

# 8. Set Comprehension
# Similar to list comprehensions but with sets
set_comp = {x for x in range(10) if x % 2 == 0}  # {0, 2, 4, 6, 8}

# 9. Conversion to and from Other Data Types
my_list = [1, 2, 3, 1, 2, 4]
list_to_set = set(my_list)  # {1, 2, 3, 4}
set_to_list = list(list_to_set)  # [1, 2, 3, 4]

# Note: Sets in Python are unordered collections with no duplicate elements.

# Set Operations using Operators in Python with operators

# Initializing sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Union (|)
# Combines elements from both sets, no duplicates
union_set = set1 | set2
print("Union of set1 and set2:", union_set)  # Output: {1, 2, 3, 4, 5, 6}

# Intersection (&)
# Elements common to both sets
intersection_set = set1 & set2
print("Intersection of set1 and set2:", intersection_set)  # Output: {3, 4}

# Difference (-)
# Elements in set1 but not in set2
difference_set = set1 - set2
print("Difference of set1 and set2:", difference_set)  # Output: {1, 2}

# Symmetric Difference (^)
# Elements in set1 or set2 but not in both
symmetric_difference_set = set1 ^ set2
print("Symmetric Difference of set1 and set2:", symmetric_difference_set)  # Output: {1, 2, 5, 6}

# Note: These operators provide a more concise way to perform set operations compared to methods.

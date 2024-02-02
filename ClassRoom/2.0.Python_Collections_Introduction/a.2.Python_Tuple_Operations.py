# Tuple Operations in Python

# 1. Initialization
my_tuple = (1, 2, 3, 4)

# 2. Accessing Elements
# Tuples support indexing and slicing just like lists
element = my_tuple[0]  # Access the first element
sub_tuple = my_tuple[1:3]  # Slice the tuple

# 3. Length of Tuple
# To find out how many elements are in the tuple
length = len(my_tuple)

# 4. Looping Through Tuple
# Tuples can be iterated through just like lists
for item in my_tuple:
    print(item)

# 5. Checking Existence
# Check if an element exists within the tuple
if 3 in my_tuple:
    print("3 is in the tuple")

# 6. Count
# Count the number of occurrences of a specific value
count = my_tuple.count(2)

# 7. Index
# Find the index of a specific value
index = my_tuple.index(3)

# 8. Concatenation
# Tuples can be concatenated using the + operator
another_tuple = (5, 6)
combined_tuple = my_tuple + another_tuple

# 9. Repetition
# Tuples support repetition using the * operator
repeated_tuple = my_tuple * 2

# Note: Tuples are immutable, so operations like append, extend, or remove are not supported.

# Example of Unpacking a Tuple
a, b, c, d = my_tuple
print("Unpacked:", a, b, c, d)

# Nested Tuples
nested_tuple = (1, (2, 3), 4)
print("Nested tuple:", nested_tuple)

# Converting List to Tuple
my_list = [1, 2, 3]
list_to_tuple = tuple(my_list)
print("List to tuple:", list_to_tuple)

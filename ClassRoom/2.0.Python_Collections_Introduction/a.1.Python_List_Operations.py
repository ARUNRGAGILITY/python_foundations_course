# List Operations in Python

# 1. Initialization
my_list = [1, 2, 3, 4]

# 2. Adding Elements
my_list.append(5)  # Append a single element at the end
my_list.insert(1, 'a')  # Insert an element at a specific index
my_list.extend([6, 7])  # Extend the list with elements from another iterable

# 3. Removing Elements
my_list.remove('a')  # Remove a specific element
del my_list[0]  # Remove element at a specific index
last_element = my_list.pop()  # Remove and return the last element

# 4. Accessing Elements
first_element = my_list[0]  # Access by index
last_element = my_list[-1]  # Access last element

# 5. Slicing
sub_list = my_list[1:3]  # Get a slice from the list

# 6. Modifying Elements
my_list[1] = 'b'  # Change the element at a specific index

# 7. Length of List
length = len(my_list)  # Get the number of elements in the list

# 8. Looping Through List
for item in my_list:
    print(item)  # Print each element in the list

# 9. Checking Existence
if 3 in my_list:
    print("3 is in the list")

# 10. List Concatenation
another_list = [8, 9, 10]
combined_list = my_list + another_list

# 11. Copying a List
list_copy = my_list.copy()

# 12. Clearing the List
my_list.clear()

# 13. Sorting the List (in-place)
my_list = [3, 1, 4, 2]
my_list.sort()

# 14. Reversing the List (in-place)
my_list.reverse()

# Note: Lists in Python are mutable, meaning they can be changed after their creation.
# List comprehension
# Example: Creating a list of squares of numbers from 0 to 4
squares = [x**2 for x in range(5)]
print(squares)  # Output: [0, 1, 4, 9, 16]

# Example: Filtering even numbers from a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)  # Output: [2, 4, 6, 8]

# Example: Creating a list of words with more than 3 characters
words = ["apple", "banana", "cherry", "date", "fig"]
long_words = [word for word in words if len(word) > 3]
print(long_words)  # Output: ['apple', 'banana', 'cherry']

# Example: Generating a list of tuples from two lists
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
combined_list = [(x, y) for x in list1 for y in list2]
print(combined_list)  # Output: [(1, 'a'), (1, 'b'), (1, 'c'), (2, 'a'), (2, 'b'), (2, 'c'), (3, 'a'), (3, 'b'), (3, 'c')]

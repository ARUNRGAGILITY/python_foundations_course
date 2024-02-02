# Python Operators Overview

'''
Arithmetic operators: +, -, /, *, **, //, %
Comparison/Relational operators: >, <, >=, <=, ==, !=
Assignment Operators:
Identity Operators:
Membership Operators:
Bitwise Operators:
Walrus Operator:
'''
#--------------------------------------------------------#
# Arithmetic Operators
a = 10
b = 3

# Addition
addition = a + b
print("Addition:", addition)  # 13

# Subtraction
subtraction = a - b
print("Subtraction:", subtraction)  # 7

# Multiplication
multiplication = a * b
print("Multiplication:", multiplication)  # 30

# Division (float)
division = a / b
print("Division:", division)  # 3.333...

# Floor Division (integer division)
floor_division = a // b
print("Floor Division:", floor_division)  # 3

# Modulus (remainder)
modulus = a % b
print("Modulus:", modulus)  # 1

# Exponentiation (power)
exponentiation = a ** b
print("Exponentiation:", exponentiation)  # 1000

#--------------------------------------------------------#
# Relationship / Comparison Operators
x = 5
y = 10

# Equal to
print("x == y is", x == y)  # False

# Not equal to
print("x != y is", x != y)  # True

# Greater than
print("x > y is", x > y)  # False

# Less than
print("x < y is", x < y)  # True

# Greater than or equal to
print("x >= y is", x >= y)  # False

# Less than or equal to
print("x <= y is", x <= y)  # True

# Logical Operators
a = True
b = False

#--------------------------------------------------------#
# Logical AND
print("a and b is", a and b)  # False

# Logical OR
print("a or b is", a or b)  # True

# Logical NOT
print("not a is", not a)  # False

#--------------------------------------------------------#
# Assignment Operators
# Basic Assignment Operator
x = 10
print("x =", x)  # x = 10

# Add and Assign: x += y is equivalent to x = x + y
x += 5
print("After x += 5, x =", x)  # x = 15

# Subtract and Assign: x -= y is equivalent to x = x - y
x -= 3
print("After x -= 3, x =", x)  # x = 12

# Multiply and Assign: x *= y is equivalent to x = x * y
x *= 2
print("After x *= 2, x =", x)  # x = 24

# Divide and Assign: x /= y is equivalent to x = x / y
x /= 4
print("After x /= 4, x =", x)  # x = 6.0

# Floor Division and Assign: x //= y is equivalent to x = x // y
x //= 3
print("After x //= 3, x =", x)  # x = 2.0

# Modulus and Assign: x %= y is equivalent to x = x % y
x %= 1.5
print("After x %= 1.5, x =", x)  # x = 0.5

# Exponent and Assign: x **= y is equivalent to x = x ** y
x **= 3
print("After x **= 3, x =", x)  # x = 0.125

# Membership Operators
list = [1, 2, 3, 4, 5]

# In
print("3 in list is", 3 in list)  # True

# Not in
print("6 not in list is", 6 not in list)  # True

#--------------------------------------------------------#
# Identity Operators
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

# is
print("x is z is", x is z)  # True, becuase z and x are same memory

# is not
print("x is not y is", x is not y)  # True (because x and y are different objects, 
#even if their contents are the same) not in same memory

#--------------------------------------------------------#
# Bitwise Operators
p = 6  # 110 in binary
q = 2  # 010 in binary

# Bitwise AND
print("p & q is", p & q)  # 2 (010)

# Bitwise OR
print("p | q is", p | q)  # 6 (110)

# Bitwise XOR
print("p ^ q is", p ^ q)  # 4 (100)

# Bitwise NOT
print("~p is", ~p)  # -7

# Bitwise left shift
print("p << 1 is", p << 1)  # 12 (1100)

# Bitwise right shift
print("p >> 1 is", p >> 1)  # 3 (011)

#--------------------------------------------------------#
# Python Walrus Operator (:=) Example

# Example 1: Using walrus operator in a while loop
# This allows you to assign and check the value in the same line
numbers = []
while (n := len(numbers)) < 5:
    print(f"Length of list is {n}, adding an element.")
    numbers.append(n)
# The while loop continues until the length of the list reaches 5

# Example 2: Using walrus operator in an if statement
# Useful for checking and assigning a value in the same condition
data = "Hello"
if (length := len(data)) > 5:
    print(f"Data is too long ({length} characters).")
else:
    print(f"Data is of acceptable length ({length} characters).")

# Example 3: Using walrus operator in a list comprehension
# It allows you to use the assigned value inside the comprehension
data_list = ["apple", "banana", "cherry", "date"]
short_fruits = [(f, len(f)) for f in data_list if (len_f := len(f)) < 6]
# This creates a list of tuples with fruit names and their lengths, but only if the length is less than 6

# Example 4: Using walrus operator for input handling
# Assign and check input in a single line
while (user_input := input("Enter a number (or 'quit' to exit): ")) != "quit":
    print(f"You entered: {user_input}")
# The loop will continue until the user enters 'quit'

# Note: The walrus operator is only available in Python 3.8 and later versions.

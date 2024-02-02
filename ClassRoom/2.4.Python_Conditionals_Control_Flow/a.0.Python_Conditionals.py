# Python Conditional Statements

#########################################################
# Python Conditionals
'''
In Python, conditional statements are used to make decisions in your code. 
They allow your program to execute different code blocks based on 
whether certain conditions are met. 
Python supports the following conditional statements:

If Statement: The if statement is used to execute a block of code 
if a specified condition is True. It can be followed by one or more 
elif (else if) statements and an optional else statement.

##-- if else --##
if condition:
    # Code to execute if the condition is True
elif another_condition:
    # Code to execute if the first condition is False and this condition is True
else:
    # Code to execute if none of the above conditions are True

# Ternary
#  value_if_true if condition else value_if_false    
    
#-- Nested if --##
if condition1:
    if condition2:
        # Code to execute when both conditions are True
    else:
        # Code to execute when condition1 is True but condition2 is False
else:
    # Code to execute when condition1 is False

'''

# Simple if
age = 18
if age >= 18:
    print("You are an adult.")
else:
    print("You are not an adult.")

# Ternary
#  value_if_true if condition else value_if_false
age = 20
message = "You are an adult" if age >= 18 else "You are not an adult"
print(message)

# Nested if statement
user_role = "admin"
if user_role == "admin":
    access_level = "Full Access"
else:
    if user_role == "editor":
        access_level = "Edit Access"
    else:
        access_level = "Read-Only Access"
print("Your access level is:", access_level)

# Validation conditions 
user_input = 15
if 1 <= user_input <= 10:
    print("Valid input.")
else:
    print("Invalid input. Please enter a number between 1 and 10.")

# checking empty string
user_input = ""
if not user_input:
    print("The string is empty.")
else:
    print("The string is not empty.")

# Match case 
'''
Starting from Python 3.10, you can use the match statement 
(also known as pattern matching) to perform structured pattern matching. 
The match statement allows you to compare a value against multiple patterns 
and execute code based on the first matching pattern. Here's how it works:

match value:
    case pattern_1:
        # Code to execute if value matches pattern_1
    case pattern_2:
        # Code to execute if value matches pattern_2
    ...
    case pattern_n:
        # Code to execute if value matches pattern_n
    case _:
        # Code to execute for the default case (optional)


Here are some key points about the match statement:

The match statement compares the value against each case pattern sequentially, 
and the first matching pattern's associated code block is executed.
You can have multiple case blocks to handle different patterns.
You can use _ as a wildcard pattern to match any value.
If none of the patterns match and there's a case _, the code in the default case is executed.
Patterns can include literals, variables, and more complex patterns.
'''
shape = "circle"
match shape:
    case "circle":
        print("It's a circle.")
    case "triangle":
        print("It's a triangle.")
    case "square":
        print("It's a square.")
    case _:
        print("Unknown shape.")

'''
In this example, the match statement checks the shape variable against 
different patterns to identify the type of shape.

The match statement is a powerful addition to Python for handling 
complex conditional logic and pattern-based matching in a more structured 
and readable way. It can be used in various scenarios to simplify code 
that involves multiple conditional checks.
'''
# Example with wild card
grade = "B"
match grade:
    case "A" | "B":
        print("Pass")
    case "C":
        print("Average")
    case "D":
        print("Fail")
    case _:
        print("Invalid grade.")

# Example with data classes
from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

point = Point(1, 2)
match point:
    case Point(0, 0):
        print("Origin")
    case Point(x=0, y=y):
        print(f"X-axis at y={y}")
    case Point(x=x, y=0):
        print(f"Y-axis at x={x}")
    case _:
        print("Arbitrary point")

# Matching with List and Tuples
data = [1, (2, 3), 4]
match data:
    case [1, (2, 3), 4]:
        print("Full match")
    case [1, _, _]:
        print("Partial match with the first element as 1")
    case [_, (2, 3), _]:
        print("Partial match with the second element as (2, 3)")
    case _:
        print("No match")

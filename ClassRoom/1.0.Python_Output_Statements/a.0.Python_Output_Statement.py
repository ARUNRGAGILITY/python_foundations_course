# Python Output Statement / Print function
'''
The print() function in Python is one of the most basic and 
frequently used functions for output. It is used to send 
data to the standard output device, which is typically 
the console or terminal or file
'''
# Python can print via print function, strings and expressions

# Printing string
# Python print function can print strings with ', ", """ single, double, triple quotes
print('Hello Python!')
print("Hello Python!")
print("""Hello Python!""")

single_line_text = "This is a single line text"
multi_line_text = """
This is a multi-line text
having
line1
line2
line3
I love Python Programming
"""

another_multi_line_text = '''
This is a multi-line text
having
line1
line2
line3
I love Python Programming
'''

print(single_line_text)
print(multi_line_text)
# Basic print to console
print("Hello, World!\n")

# Formatted print using .format()
name = "Anjali"
print("Hello, {}!".format(name))

# Formatted print using f-string (Python 3.6+)
age = 30
print(f"{name} is {age} years old")

# Printing multiple items: multiple data-types
print("Name:", name, "- Age:", age)

# Writing to a file
with open("output.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("Hello, {}!\n".format(name))
    file.write(f"{name} is {age} years old\n")
    file.write(f"Name: {name} - Age: {age}\n")

# Printing with a separator
print("Apple", "Banana", "Cherry", "Pineapple", "Gauva", sep=", ")

# Printing with end parameter
print("This is on one line", end=", ")
print("and this continues on the same line")

# Writing a list to a file with join
fruits = ["Apple", "Banana", "Cherry"]
with open("fruits1.txt", "w") as file:
    file.write(", ".join(fruits))

# Note: The file outputs will not be visible on the console.
# They will be written to 'output.txt' and 'fruits.txt' in the current directory.

# Printing with commas, mixing data types, and using expressions

# Basic variables with different data types
name = "John"
age = 32
height = 5.8  # in feet

# Basic print with comma separation
print("Name:", name, "Age:", age, "Height:", height)

# Printing expressions
print("In ten years,", name, "will be", age + 10, "years old.")

# Mixing data types
is_student = False
is_employee = True
print(name, "is a student:", is_student)
print(name, "is a is_employee:", is_employee)
# Using mathematical expressions
number_of_apples = 5
number_of_oranges = 3
number_of_mangoes = 4
print("Total fruits:", number_of_apples + number_of_oranges + number_of_mangoes)

# Printing with a mix of strings and numbers
print(name, "is", age, "years old and", height, "feet tall.")

# Printing float numbers
# Example: Rounding off decimal numbers

# Define a float number
float_number = 3.14159265

# Round to 2 decimal places
rounded_two = round(float_number, 2)
print("Rounded to 2 decimal places:", rounded_two)

# Round to 4 decimal places
rounded_four = round(float_number, 4)
print("Rounded to 4 decimal places:", rounded_four)

# Round to no decimal places (integer)
rounded_no_decimal = round(float_number)
print("Rounded to no decimal places:", rounded_no_decimal)


# Note: In these print statements, Python automatically adds a space between items when using a comma.

'''
Escape sequences in Python are used within strings to 
represent certain special characters that are not 
easily represented in string literals. 

Each escape sequence starts with a backslash (\) followed by a 
character that signifies a particular action, 
like a newline (\n), tab (\t), or a literal character 
like a single quote (\'). These sequences allow you to 
include such special characters in strings that 
would otherwise be difficult to express directly.
'''
# Escape sequence examples in Python

# Newline
print("Hello\nWorld")

# Tab
print("Hello\tWorld")

# Backslash
print("This is a backslash: \\")

# Single quote
print('It\'s a sunny day')

# Double quote
print("He said, \"Hello!\"")

# Carriage return
print("Hello\rWorld")

# Backspace
print("Hello\bWorld")

# Form feed
print("Hello\fWorld")

# Octal value (example: \o12 represents a newline)
print("\o12")

# Hex value (example: \x0a represents a newline)
print("\x0a")

# Unicode character (example: \u2764 represents a heart)
print("\u2764")

# Note: When you run this code, you'll see the effect of each escape sequence in the output.

# Printing Date and time
'''
Printing Date and Time
'''
from datetime import datetime

# Get the current date and time
current_datetime = datetime.now()

# Print the current date and time
print("Current Date and Time:", current_datetime)

# Print individual components (year, month, day, hour, minute, second)
print("Year:", current_datetime.year)
print("Month:", current_datetime.month)
print("Day:", current_datetime.day)
print("Hour:", current_datetime.hour)
print("Minute:", current_datetime.minute)
print("Second:", current_datetime.second)




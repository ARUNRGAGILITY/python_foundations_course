# Python Input Statement

# Python input() function examples

# Basic input
name = input("Enter your name: ")
print("Hello,", name + "!")

# Input with prompt for an integer
# Note: input() function returns a string, so we need to convert it to an integer
age = int(input("Enter your age: "))
print("You are", age, "years old.")

# Input with prompt for a float
height = float(input("Enter your height in meters: "))
print("Your height is", height, "meters.")

# Boolean input
# Python doesn't have a built-in way to input booleans, so we use a string and compare
likes_python = input("Do you like Python? (yes/no): ").lower() == "yes"
print("Likes Python:", likes_python)

# Handling input errors with try-except
try:
    number = float(input("Enter a number: "))  # Using float to accept both integers and floats
    print("Your number is:", number)
except ValueError:
    print("That's not a valid number!")

# Taking a list of values as input
# Note: This will take the entire line as a string and then split it into a list
numbers_list = input("Enter a few numbers separated by space: ").split()  # Splitting the input string into a list
print("You entered:", numbers_list)

# Note: To run these examples, you will need to enter the values in the console when prompted.

# Python input() function examples with different choices

# Example: Basic string input
favorite_color = input("What is your favorite color? ")
print("Your favorite color is:", favorite_color)

# Example: Choosing from a list of options
season_options = """
Choose your favorite season:
1. Spring
2. Summer
3. Autumn
4. Winter
"""
print(season_options)
season_choice = input("Enter the number of your choice: ")
print("You chose:", season_choice)

# Example: Yes or No question
study_python = input("Are you currently studying Python? (yes/no) ").lower()
if study_python == 'yes':
    print("Great! Keep learning Python.")
else:
    print("Python is a great language to start learning!")

# Example: Numeric input
birth_year = int(input("Enter your birth year: "))
current_year = 2024
age = current_year - birth_year
print("You are approximately", age, "years old.")

# Example: Multi-choice input with single letter
pet_options = """
What is your preferred pet?
a. Dog
b. Cat
c. Bird
d. Fish
"""
print(pet_options)
pet_choice = input("Enter a, b, c, or d: ").lower()
if pet_choice == 'a':
    print("You prefer dogs.")
elif pet_choice == 'b':
    print("You prefer cats.")
elif pet_choice == 'c':
    print("You prefer birds.")
elif pet_choice == 'd':
    print("You prefer fish.")
else:
    print("Invalid choice.")

# Example: Free text input
dream_destination = input("Where would you like to travel the most? ")
print("Your dream travel destination is:", dream_destination)

# Note: To use these examples, run the code and input your responses when prompted.

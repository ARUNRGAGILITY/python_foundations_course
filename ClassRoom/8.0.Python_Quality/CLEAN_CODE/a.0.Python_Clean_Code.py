# Clean Code approach 
'''
Meaningful Names and Functions: The function calculate_average_temperatures 
has a self-explanatory name and a clear purpose.

Clear and Concise Comments: The is_prime function is documented with a 
docstring explaining its purpose, arguments, and return value.

Avoiding Deep Nesting: The process_data function processes data without 
deep nesting, making the code easier to read.

Code Reusability and DRY Principle: The greet_user and farewell_user 
functions demonstrate reusability and the DRY principle.

Descriptive Variable Names: In find_longest_word, the variable 
names clearly describe what they store.

Error Handling with Exceptions: The divide_numbers function 
gracefully handles division by zero using exceptions.

Code Formatting (PEP 8): The Animal class follows PEP 8 styling 
guidelines, which is the standard for Python code formatting.


'''

# Importing necessary libraries
from typing import List

# Meaningful Names and Functions
def calculate_average_temperatures(temperatures: List[float]) -> float:
    return sum(temperatures) / len(temperatures)

# Clear and Concise Comments
def is_prime(number: int) -> bool:
    """
    Check if a number is a prime number.

    A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.

    Args:
    number (int): The number to check.

    Returns:
    bool: True if the number is prime, False otherwise.
    """
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

# Avoiding Deep Nesting
def process_data(data: List[int]) -> List[int]:
    processed_data = []
    for value in data:
        if value > 0:
            processed_data.append(value * 2)
    return processed_data

# Code Reusability and DRY (Don't Repeat Yourself)
def greet_user(username: str) -> None:
    print(f"Hello, {username}!")

def farewell_user(username: str) -> None:
    print(f"Goodbye, {username}!")

# Using Descriptive Variable Names
def find_longest_word(words: List[str]) -> str:
    longest_word = ''
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word

# Error Handling with Exceptions
def divide_numbers(numerator: float, denominator: float) -> float:
    try:
        return numerator / denominator
    except ZeroDivisionError:
        print("Cannot divide by zero")
        return float('inf')

# Code Formatting (PEP 8)
class Animal:
    def __init__(self, species: str, legs: int):
        self.species = species
        self.legs = legs

    def display_info(self):
        print(f"The {self.species} has {self.legs} legs")

# Demonstrating the clean code functions
temperatures = [22.4, 23.1, 19.8]
print("Average Temperature:", calculate_average_temperatures(temperatures))

number = 17
print(f"Is {number} a prime number? {is_prime(number)}")

data = [-1, 2, -3, 4]
print("Processed Data:", process_data(data))

greet_user("Alice")
farewell_user("Bob")

words = ["Python", "Development", "Clean", "Code"]
print("Longest Word:", find_longest_word(words))

result = divide_numbers(10, 0)

animal = Animal("Dog", 4)
animal.display_info()

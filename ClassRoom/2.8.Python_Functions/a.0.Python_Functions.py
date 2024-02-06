# Python Functions Basics

# Defining a simple function
def greet():
    # This function prints a greeting
    print("Hello, World!")

# Calling the function
greet()  # Output: Hello, World!

# Function with parameters
def greet_person(name):
    # Greets a person with the given name
    print(f"Hello, {name}!")

# Calling the function with an argument
greet_person("John")  # Output: Hello, Alice!

# Function with return value
def add_numbers(a, b):
    # Returns the sum of two numbers
    return a + b

# Calling the function and printing its return value
result = add_numbers(5, 3)
print("The sum is:", result)  # Output: The sum is: 8

# Function with default parameters
def greet_friend(name="Friend"):
    # Greets a person; defaults to "Friend" if no name is given
    print(f"Hello, {name}!")

# Calling function with and without an argument
greet_friend("Bob")  # Output: Hello, Bob!
greet_friend()       # Output: Hello, Friend!

# Function with keyword arguments
def describe_pet(animal_type, pet_name):
    # Describes a pet with the given type and name
    print(f"I have a {animal_type} named {pet_name}.")

# Calling function using keyword arguments
describe_pet(animal_type="hamster", pet_name="Harry")
# Output: I have a hamster named Harry.

# Function with variable number of arguments (*args)
def make_pizza(*toppings):
    # Prints the list of toppings for a pizza
    print("Making a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

# Calling function with variable arguments
make_pizza("pepperoni")
make_pizza("mushrooms", "green peppers", "extra cheese")
# Output: Making a pizza with the following toppings:
# - mushrooms
# - green peppers
# - extra cheese

# Function with variable keyword arguments (**kwargs)
def build_profile(first, last, **user_info):
    # Builds a dictionary containing user information
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

# Calling function with variable keyword arguments
user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)
# Output: {'first_name': 'albert', 'last_name': 'einstein', 'location': 'princeton', 'field': 'physics'}

# Note: The above examples cover the basics of defining and using functions in Python.

# Python Decorator, Lambda, and Inner Function Examples

# Decorator Function
def my_decorator(func):
    # A wrapper function that modifies the behavior of func
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

# Calling the decorated function
say_hello()
# Output: 
# Something is happening before the function is called.
# Hello!
# Something is happening after the function is called.

# Lambda Function
# A simple lambda function to add two numbers
add = lambda x, y: x + y

# Using the lambda function
print("Sum:", add(5, 3))  # Output: Sum: 8

# Inner Function
def print_msg(message):
    # An outer function that defines an inner function
    def printer():
        # An inner function that uses a variable from the outer function
        print(message)
    printer()

# Calling the function with inner function
print_msg("Hello from the inner function!")
# Output: Hello from the inner function!

# Note: 
# - A decorator function is used to modify the behavior of another function.
# - Lambda functions are small anonymous functions defined with the lambda keyword.
# - Inner functions are functions defined inside other functions.


def multiply_nos(n1=1, n2=1, n3=1):
    result = n1 * n2 * n3
    return result


result = multiply_nos()
print(result)

'''
Decorator functions in Python are used to modify or extend the 
behavior of other functions or methods. They are a powerful tool 
for adding functionality to existing code in a clean, readable way. 
Decorators are particularly useful in scenarios where you want to apply 
the same change to several functions or methods.

Decorators wrap around a function, allowing you to execute code 
before and after the wrapped function runs, without modifying 
the function itself.
This is useful for logging, enforcing access control and 
authentication, instrumentation, modifying function arguments 
or return values, and more.
Decorators can be applied to any callable in Python 
(functions, methods, classes).
'''

'''
Lambda functions, also known as anonymous functions, 
are used for creating small, one-off functions in 
Python with a single expression. They are useful i
n situations where a simple function is required for a 
short period, and defining a standard function with a 
def statement would be overkill and less readable.

Lambda functions are defined using the lambda keyword.
They can take any number of arguments but can only have one expression.
The expression is evaluated and returned automatically.
Lambda functions are often used in places where a simple function is 
required for a short duration, without the need to formally define a function.
'''

# Generators

'''
Generators in Python are a simple and powerful tool for 
creating iterators. They are written like regular functions 
but use the yield statement whenever they want to return data. 
Each time yield is called, the generator resumes where it left 
off (it remembers all the data values and which statement 
was last executed). This is a more memory-efficient way of 
writing iterators.

Generators are ideal for:

Handling large data sets
Streaming data
Pipelining data transformations
On-the-fly calculation
Remember, generators are a one-time use object. 
Once they have been iterated through, they cannot be restarted or reused. 
For a new iteration, you need to create a new generator object.
'''
# Generator function to yield squares of numbers up to a given limit
def generate_squares(limit):
    for i in range(limit):
        yield i * i  # Yield the square of the number

# Using the generator
for square in generate_squares(5):
    print(square)

# Another example
# Generator to generate Fibonacci numbers
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Using the generator
for fib_number in fibonacci(10):
    print(fib_number)


# Generator calling again for next time (after its one time usage)
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# First iteration
fib_gen = fibonacci(10)
for num in fib_gen:
    print(num)

# Creating a new generator object for second iteration
fib_gen = fibonacci(10)
print("\nStarting second iteration:")
for num in fib_gen:
    print(num)

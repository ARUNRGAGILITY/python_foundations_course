# Python Functions
In Python, functions are defined using the `def` keyword and are used to encapsulate a set of instructions that can be executed multiple times. Functions allow for code reuse, organization, and better readability.

### Basic Syntax of a Function

```python
def function_name(parameters):
    """Docstring describing the function"""
    # Function body
    return result  # Optional return statement
```

### Key Points

1. **Defining a Function:**
   - Use `def` followed by the function name and parentheses `()`.
   - Parameters (arguments) through which we pass values to a function are placed inside these parentheses.
   - The function body starts with a colon `:` and is indented.

2. **Docstring:**
   - The first string after the function header is called the docstring and is short for documentation string.
   - Although optional, docstrings are a good practice.

3. **Return Statement:**
   - `return` statement is used to exit a function and go back to the place from where it was called, optionally returning a value.
   - A function without a `return` statement returns `None`.

4. **Calling a Function:**
   - To call a function, use the function name followed by parentheses.

### Examples

#### Basic Function

```python
def greet(name):
    """This function greets the person passed in as a parameter"""
    return "Hello, " + name

print(greet("John"))
```

#### Function with Multiple Parameters

```python
def add_numbers(x, y):
    return x + y

result = add_numbers(5, 3)
print(result)  # Output: 8
```

#### Function with Default Parameter Value

```python
def greet(name, msg="Good morning!"):
    return f"Hello {name}, {msg}"

print(greet("Kate"))  # Uses default message
print(greet("Bruce", "How do you do?"))  # Overrides default message
```

### Scope of Variables

Variables defined inside a function are not accessible from outside the function. These are called local variables. However, a function can access variables defined outside the function, which are known as global variables.

### Functions as First-Class Citizens

In Python, functions are first-class citizens, meaning they can be passed as arguments to other functions, returned as values from other functions, and assigned to variables.



### 1. Beginner: Basic Greeting Function

```python
def greet(name):
    """Greets a person with their name."""
    return f"Hello, {name}!"

print(greet("Alice"))
```

### 2. Beginner: Function with Default Parameters

```python
def describe_pet(pet_name, animal_type='dog'):
    """Describes a pet."""
    return f"I have a {animal_type} and its name is {pet_name}."

print(describe_pet("Rex"))
print(describe_pet("Whiskers", "cat"))
```

### 3. Intermediate: Function with Arbitrary Number of Arguments

```python
def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    return f"Making a pizza with {', '.join(toppings)}."

print(make_pizza("pepperoni"))
print(make_pizza("mushrooms", "green peppers", "extra cheese"))
```

### 4. Intermediate: Function with Keyword Arguments

```python
def build_profile(first, last, **user_info):
    """Builds a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)
```

### 5. Intermediate: Recursive Function for Fibonacci Sequence

```python
def fibonacci(n):
    """Return the nth value in the fibonacci series."""
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))
```

### 6. Advanced: Lambda Functions

```python
# Lambda function to multiply two values
multiply = lambda x, y: x * y
print(multiply(5, 6))
```

### 7. Advanced: Decorators

```python
def decorator_function(original_function):
    def wrapper_function():
        print(f"{original_function.__name__} is being executed!")
        return original_function()
    return wrapper_function

@decorator_function
def display():
    return "Display function ran."

print(display())
```

### 8. Advanced: Function Returning Another Function

```python
def main_function(msg):
    def inner_function():
        print(f"Message is: {msg}")
    return inner_function

fun = main_function("Hello, World!")
fun()
```

### 9. Advanced: Generators

```python
def simple_generator():
    yield 1
    yield 2
    yield 3

for value in simple_generator():
    print(value)
```

### 10. Advanced: Higher Order Functions

```python
def log_message(func):
    def wrapper(*args, **kwargs):
        print(f"Logging: {func.__name__} was called")
        return func(*args, **kwargs)
    return wrapper

@log_message
def add(x, y):
    """Adds two numbers."""
    return x + y

print(add(5, 7))
```




# Class: Python Variables

'''
Python Keywords / Reserved Words for Programming in Python
>>> help("keywords")

Here is a list of the Python keywords.  Enter any keyword to get more help.

False               class               from                or
True                def                 if                  raise
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield
break               for                 not


'''

'''
Operator Keywords: and, or, not, in, is
Control Flow Keywords: if, elif, else, match
Iteration Keywords: for, while, break, continue
Value Keywords: True, False, None
Return Keywords: return, yeild
Import Keywords: import, from, as
Exception Handling Keywords: try, except,raise, finally, else, assert
Asynchronous Keywords: async, await
Variable Keywords: del, global, nonlocal

You can print by going to REPL
>>> python
>>> import keyword
>>> print(len(keyword.kwlist))
>>> for kw in keyword.kwlist:
    .... print(kw)
'''

# Python Variable Naming Rules

'''
Do's and Don'ts
Variable names can include letters, numbers, and underscores
Variable names cannot start with a number
Spaces are not allowed in variable names
Variable names are case-sensitive (meaning 'myVar' and 'myvar' are different variables)
Variable names cannot be the same as Python reserved keywords

Good Practices
It's best practice to use descriptive names for readability, snake case preferred user_first_name, user_full_name
Avoid using single character variables except for very short code blocks or counters in loops
Constants (variables that are not supposed to change) are usually named using all uppercase letters
'''

# Rule 1: Variable names can include letters, numbers, and underscores
valid_variable_1 = "This is valid"
variable123 = "Also valid"

# Rule 2: Variable names cannot start with a number
# 1st_variable = "Invalid - starts with a number"  # Uncommenting this will cause a syntax error

# Rule 3: Spaces are not allowed in variable names
# my variable = "Invalid"  # Uncommenting this will cause a syntax error

# Rule 4: Variable names are case-sensitive (meaning 'myVar' and 'myvar' are different variables)
myVar = "Var1"
myvar = "Var2"
print("myVar:", myVar)
print("myvar:", myvar)

# Rule 5: Variable names cannot be the same as Python reserved keywords
# Examples of keywords: False, None, True, if, else, elif, for, while, break, continue, etc.
# true = "Invalid"  # Uncommenting this will cause a syntax error

# Rule 6: It's best practice to use descriptive names for readability
customer_name = "John Doe"  # Descriptive naming
x = "John Doe"  # Less descriptive

# Rule 7: Use underscores for multi-word variable names (snake_case)
first_name = "John"
last_name = "Doe"

# Rule 8: Avoid using single character variables except for very short code blocks or counters in loops
for i in range(5):
    print(i)

# Rule 9: Constants (variables that are not supposed to change) are usually named using all uppercase letters
PI = 3.14159
MAX_SIZE = 100

# These rules help in writing clean, understandable, and maintainable code in Python.

# Python Variable Scopes

'''
Local Scope: Variables defined within a function are accessible only within that function.
Enclosing Scope: Variables in the enclosing scope are accessible from an inner, nested function.
Global Scope: Variables defined at the top level of a script or module are accessible throughout the code.
Built-in Scope: These are special names that Python reserves for itself (like print, len).
'''
# Python Variable Scope Examples

# Global scope
global_var = "I am a global variable"

def outer_function():
    # Enclosing scope
    enclosing_var = "I am an enclosing variable"

    def inner_function():
        # Local scope
        local_var = "I am a local variable"

        print("From inner_function",local_var)  # Accessing the local variable
        print("From inner_function",enclosing_var)  # Accessing the enclosing variable
        print("From inner_function", global_var)  # Accessing the global variable

    inner_function()

# Calling the function
outer_function()

# Accessing the global variable
print(global_var)

# This will cause an error if uncommented, as enclosing_var is not in this scope
# print(enclosing_var)

# This will also cause an error if uncommented, as local_var is not in this scope
# print(local_var)

'''
global_var is defined in the global scope and can be accessed anywhere in the module.
enclosing_var is defined in the enclosing scope of outer_function and is accessible within outer_function and inner_function.
local_var is defined in the local scope of inner_function and can only be accessed within this function.

Attempting to access enclosing_var or local_var outside their respective scopes will result in an error.
'''
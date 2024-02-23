# Python Comments Classroom Session

# This is a single-line comment
print("Hello, World!")  # This comment is after a code statement

# This is a multi-line comment with """" triple double quotes
"""
This is a multi-line comment
It spans multiple lines
"""
print("Hello, World!")

# This is a multi-line comment with ''' triple single quotes
'''
This is a multi-line comment
It spans several lines
'''
print("Hello, world!")


# Docstring accessed with funtion_name.__doc__
def greet(name):
    """
    Greet function Documentation: 
    This function greets the person passed in as a parameter
    """
    print("Hello, " + name)

print(greet.__doc__)
# Function with Doc String example
def my_function():
    """This is a docstring for the my_function testing."""
    pass

print(my_function.__doc__)

# Class Example with doc string
class Myclass:
    """This is a docstring for Myclass."""

    def my_method(self):
        """This is a docstring for my_method of Myclass."""
        pass

print(Myclass.__doc__)
print(Myclass.my_method.__doc__)
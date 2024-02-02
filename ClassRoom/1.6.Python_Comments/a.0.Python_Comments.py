# Python Comments Classroom Session

# This is a single-line comment
print("Hello, World!")  # This comment is after a code statement

"""
This is a multi-line comment
It spans multiple lines
"""
print("Hello, World!")

# Docstring accessed with funtion_name.__doc__
def greet(name):
    """This function greets the person passed in as a parameter"""
    print("Hello, " + name)
# Function with Doc String example
def my_function():
    """This is a docstring for the my_function."""
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
from functools import reduce
# A Quick Introduction of lamda, map, filter, reduce 

# lamdda: Define a lambda function that adds two numbers
add = lambda x, y: x + y
# Use the lambda function
result = add(5, 3)
print("Result:", result)

# Example list
numbers = [1, 2, 3, 4, 5]

# map: Using map to square all numbers
squared_numbers = list(map(lambda x: x**2, numbers))
print("Squared Numbers:", squared_numbers)

# filter: Using filter to get only even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even Numbers:", even_numbers)

# reduce: Using reduce to compute the sum of the numbers
sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print("Sum of Numbers:", sum_of_numbers)


# Python Lambda, map, filter, reduce

from functools import reduce

# Example list
numbers = [1, 2, 3, 4, 5]

# Lambda Function
# A lambda function is a small anonymous function.
# It can take any number of arguments, but can only have one expression.
# Syntax: lambda arguments: expression
double = lambda x: x * 2

# Using the lambda function to double each number in the list
doubled_numbers = list(map(double, numbers))
print("Doubled Numbers:", doubled_numbers)

# Map
# The map function applies a given function to each item of an iterable (like a list) and returns a list of the results.
# Syntax: map(function, iterable)
# Using lambda directly within map to triple each number
tripled_numbers = list(map(lambda x: x * 3, numbers))
print("Tripled Numbers:", tripled_numbers)

# Filter
# The filter function constructs an iterator from elements of an iterable for which a function returns true.
# Syntax: filter(function, iterable)
# Using lambda within filter to find even numbers
even_numbers = list(filter(lambda x: (x % 2 == 0), numbers))
print("Even Numbers:", even_numbers)

# Reduce
# The reduce function applies a rolling computation to sequential pairs of values in a list.
# Syntax: reduce(function, iterable)
# Using lambda within reduce to compute the product of all numbers
product_of_numbers = reduce(lambda x, y: x * y, numbers)
print("Product of Numbers:", product_of_numbers)

# Functional Programmin in Python
# A Simple Introduction

'''
map, filter, and reduce are functions in Python that enable 
functional programming paradigms. These functions allow for 
efficient data processing by applying functions to sequences 
like lists. They are particularly useful in situations involving 
collection manipulation, data analysis, or when you want to 
apply a transformation or operation to a series of elements 
in a concise manner.
'''

'''
Map function:

map Function:

Purpose: The map function applies a specified function to 
each item of an iterable (like a list or tuple) and 
returns an iterator.
Usage: It's often used when you want to transform a list 
of items by applying a function to each item. This is 
common in data transformation tasks.
Syntax: map(function, iterable)
Example: Converting temperatures from Celsius to Fahrenheit.
'''
celsius = [39.2, 36.5, 37.3, 37.8]
fahrenheit = list(map(lambda x: (9/5) * x + 32, celsius))


'''
Filter Function:

filter Function:

Purpose: The filter function constructs a list (or another iterable) 
from those elements of an iterable for which a function returns true.
Usage: It's used when you need to filter out elements of a 
sequence based on some condition. This is common in data 
cleaning or data processing tasks.
Syntax: filter(function, iterable)
Example: Filtering out even numbers from a list.
'''
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

'''
Reduce Function:

reduce Function:

Purpose: The reduce function applies a rolling computation 
to sequential pairs of values in a list. It's part of the 
functools module.
Usage: It is used when you want to cumulatively apply an 
operation to items of a list, such as summing them up or 
finding their product. This is common in operations that 
require aggregation of data points.
Syntax: reduce(function, iterable[, initializer])
Example: Calculating the product of all numbers in a list.
'''
from functools import reduce
numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)

'''
Summary:
lamdda, map, filter, reduce are used in 
data analysis, scientific computing, and web development, 
especially when working with large datasets. 
They allow for writing cleaner, more readable code, 
and can often be more efficient than traditional loops, 
particularly in conjunction with lambda functions. 
They embody the idea of "functional programming" where you 
apply functions to sequences and collections of data.
'''
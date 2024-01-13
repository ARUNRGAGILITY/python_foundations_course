# Python Output Statement
In Python, the `print()` function is commonly used for outputting information to the console. 
There are various ways to use this function, each serving different purposes or styles. Here are some of the common types along with examples:

1. **Basic Print Statement**: Prints simple messages or variable values.
   ```python
   print("Hello, World!")
   x = 10
   print(x)
   ```

2. **Print With Separator**: Uses the `sep` parameter to define how multiple objects are separated.
   ```python
   print("Hello", "World", sep=", ")
   ```

3. **Print With End Parameter**: The `end` parameter defines what is printed at the end of the statement, default is newline.
   ```python
   print("Hello", end=" ")
   print("World")
   ```

4. **Print Multiple Items**: Printing multiple items separated by spaces by default.
   ```python
   a = 5
   b = 10
   print("The values are", a, "and", b)
   ```

5. **Formatted String Literals (f-strings)**: Allows embedding expressions inside string literals using `{}`.
   ```python
   name = "Alice"
   age = 30
   print(f"My name is {name} and I am {age} years old.")
   ```

6. **Using Format Method**: Using `str.format()` for formatting strings.
   ```python
   print("The numbers are {} and {}".format(1, 2))
   print("The numbers are {1} and {0}".format(2, 1)) # Specifying order
   ```

7. **Print With File Parameter**: Redirecting the output to a file instead of the console.
   ```python
   with open("output.txt", "w") as file:
       print("Hello, file!", file=file)
   ```

8. **Printing Objects**: Directly printing objects will use the object's `__str__` or `__repr__` method.
   ```python
   class Point:
       def __init__(self, x, y):
           self.x = x
           self.y = y
       def __repr__(self):
           return f"Point({self.x}, {self.y})"

   p = Point(1, 2)
   print(p)
   ```
9. **Printing Multiline Strings**: Printing multiline strings
In Python, you can use triple quotes (`"""` or `'''`) to print multi-line strings. This is particularly useful when you want to print a string that spans several lines without inserting newline characters (`\n`) manually. Here's an example:

```python
multi_line_string = """This is a multi-line string.
It spans multiple lines.
This is the third line."""

print(multi_line_string)
```

When you run this code, it will print:

```
This is a multi-line string.
It spans multiple lines.
This is the third line.
```

Each new line in the string is automatically translated to a newline in the output. This method is very handy for printing long texts, formatted messages, or even small pieces of formatted data.
Each of these methods serves different use-cases, from simple printing to more complex output formatting. You can choose the one that best suits your needs in different situations.

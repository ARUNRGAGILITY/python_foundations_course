# Python Basic Data Types
Python has several built-in basic data types.
They are integer, float, boolean, string, complex numbers. Here's a detailed explanation of each:

1. **Integer (`int`)**:
   - Represents whole numbers without a fractional component.
   - Examples: `5`, `-3`, `42`.
   - Python supports arbitrary precision integers, meaning there's practically no limit to the number of digits.
   - Usage example:
     ```python
     x = 10
     print(type(x))  # Output: <class 'int'>
     ```

2. **Float (`float`)**:
   - Represents real numbers, including those with fractional parts.
   - Examples: `3.14`, `-0.001`, `2.0`.
   - In Python, floats are represented in double precision by default (64-bit).
   - Usage example:
     ```python
     y = 3.14
     print(type(y))  # Output: <class 'float'>
     ```

3. **String (`str`)**:
   - Used for text or sequences of characters.
   - Defined by enclosing text in single (' '), double (" "), or triple (''' ''' or """ """) quotes.
   - Strings are immutable, meaning you cannot change a string after it's created (you can only create new strings).
   - Supports indexing and slicing.
   - Usage example:
     ```python
     name = "Alice"
     print(type(name))  # Output: <class 'str'>
     ```

4. **Boolean (`bool`)**:
   - Represents two values: `True` or `False`.
   - Commonly used in conditional statements and logical operations.
   - Derived from integer type (`True` is 1, and `False` is 0).
   - Usage example:
     ```python
     is_valid = True
     print(type(is_valid))  # Output: <class 'bool'>
     ```

5. **Complex Number (`complex`)**:
   - Used for complex numbers, which include a real part and an imaginary part.
   - Imaginary part is denoted by 'j' or 'J'.
   - Examples: `3 + 4j`, `-1.5 + 2.5j`.
   - Supports arithmetic operations similar to real numbers.
   - Usage example:
     ```python
     z = 1 + 2j
     print(type(z))  # Output: <class 'complex'>
     ```

Each of these data types serves a specific purpose and is a fundamental part of Python programming. Understanding these types is crucial for effective coding, especially in data manipulation and algorithm implementation.

# Python Additonal Exercises for Basic Data Types
import math

# Integer Operations
# Absolute Value
int_num = -10
abs_val = abs(int_num)
print("Absolute Value of Integer:", abs_val)

# Power of Integer
base = 3
exponent = 4
power_result = pow(base, exponent)
print("Power Result:", power_result)

# Float Operations
# Rounding a Float
float_num = 3.14159
rounded_num = round(float_num, 2)
print("Rounded Number:", rounded_num)

# Ceiling and Floor
float_num = 2.56
ceil_val = math.ceil(float_num)
floor_val = math.floor(float_num)
print("Ceiling Value:", ceil_val)
print("Floor Value:", floor_val)

# String Operations
# String Length
my_string = "Hello, Python!"
length = len(my_string)
print("String Length:", length)

# String to Uppercase/Lowercase
uppercase = my_string.upper()
lowercase = my_string.lower()
print("Uppercase:", uppercase)
print("Lowercase:", lowercase)

# Boolean Operations
# Boolean Negation
bool_val = True
negated_val = not bool_val
print("Negated Boolean Value:", negated_val)

# Boolean as Integer
int_val = int(bool_val)
print("Boolean as Integer:", int_val)

# Complex Number Operations
# Complex Number Real and Imaginary Parts
complex_num = 3 + 4j
real_part = complex_num.real
imaginary_part = complex_num.imag
print("Real Part of Complex Number:", real_part)
print("Imaginary Part of Complex Number:", imaginary_part)

# Absolute Value of Complex Number
abs_val_complex = abs(complex_num)
print("Absolute Value of Complex Number:", abs_val_complex)

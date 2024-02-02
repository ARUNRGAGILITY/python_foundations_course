#########################################################
# Python Loop Constructs
'''
Python provides several loop constructs for iterating over sequences, 
performing repetitive tasks, and controlling the flow of your program. 
Here are the primary loop constructs in Python along with their details, 
use cases, and examples:

for Loop:

Details: The for loop is used for iterating over a sequence 
(such as a list, tuple, string, or range) and performing 
a set of actions for each item in the sequence.

Use Cases: It is commonly used when you know the number of iterations
in advance or when you want to process each item in a sequence.
'''

# Simple for loop 
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
    
#-------------------------------------------------------#
# While Loop
'''
while Loop:
Details: The while loop repeatedly executes a block of code as 
long as a specified condition is True. It is used when the 
number of iterations is not known in advance.

Use Cases: It is suitable for situations where you want to 
continue executing code until a certain condition is met.
'''
# while loop example 
count = 0
while count < 5:
    print(count)
    count += 1

#-------------------------------------------------------#
# range function
'''
range() Function:

Details: The range() function generates a sequence of numbers 
that can be used in for loops. It is often used to control 
the number of iterations.

Use Cases: It is commonly used with for loops when 
you need to iterate a specific number of times.
'''
# Simple range function example
for i in range(5):
    print(i)


## Nested loops
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in matrix:
    for element in row:
        print(element)


## Loop control 
numbers = [1, 2, 3, 4, 5, 6]
for num in numbers:
    if num % 2 == 0:
        continue  # Skip even numbers
    if num == 5:
        break  # Exit the loop when 5 is encountered
    print(num)

## List comprehensions
'''
Details: List comprehensions provide a concise way to create lists based 
on existing sequences or perform operations on elements.

Use Cases: They are used when you want to create a new list 
by applying a transformation to elements of an existing list.
'''
numbers = [1, 2, 3, 4, 5]
squares = [num ** 2 for num in numbers]
print(squares)


'''
The primary use of a `while` loop compared to a `for` loop is to 
perform iterations when the number of iterations is not known in 
advance or when you want to repeatedly execute a block of code 
as long as a specified condition remains `True`. 
Here's a breakdown of the primary use cases for a `while` loop:

1. **Unknown Number of Iterations**: `while` loops are suitable 
when you don't know in advance how many times you need to iterate.
Instead of specifying a fixed number of iterations, you specify a 
condition that determines when the loop should terminate. 
The loop continues executing until the condition becomes `False`.

   ```python
   count = 0
   while count < 5:
       print(count)
       count += 1
   ```

2. **Condition-Driven Execution**: `while` loops are useful for 
situations where you want to perform a task until a certain 
condition is met. For example, you might use a `while` loop 
to repeatedly ask a user for input until they enter a valid value.

   ```python
   user_input = ""
   while not user_input:
       user_input = input("Enter something: ")
   ```

3. **Infinite Loops**: You can intentionally create infinite loops 
using `while` when you want a piece of code to run indefinitely 
until an external event (such as user input or a signal) 
triggers the loop to exit.

   ```python
   while True:
       # This loop runs indefinitely until interrupted by an external event.
   ```

4. **Dynamic Conditions**: `while` loops allow you to evaluate 
and update conditions dynamically within the loop. This can be 
useful for scenarios where the loop should terminate based on 
changing conditions.

   ```python
   balance = 1000
   while balance > 0:
       # Continue processing transactions until the balance reaches zero or negative.
       transaction_amount = int(input("Enter transaction amount: "))
       balance -= transaction_amount
   ```

In contrast, a `for` loop is typically used when you know the number of 
iterations in advance or when you want to iterate over elements in a 
sequence (e.g., a list or tuple). The `for` loop is more structured 
and commonly used for tasks that involve iterating through collections of data.

In summary, the primary use of a `while` loop is to perform iterations 
based on a condition, making it suitable for scenarios where the number 
of iterations is not predetermined or when you need to repeatedly 
execute code until a specific condition is satisfied.
'''

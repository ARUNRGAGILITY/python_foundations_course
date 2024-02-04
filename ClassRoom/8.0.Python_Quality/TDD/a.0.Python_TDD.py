# Test Driven Development (TDD)
'''
Test-Driven Development (TDD) involves writing tests for your 
functions before you even write the code to implement those functions. 
This approach ensures that your code meets the requirements 
you've set out from the start. In Python, you can use the unittest module for this.

Here's a simple TDD example for a function that calculates the factorial of a number:

Write the Test First: Define a test case for the desired functionality.
Run the Test and See it Fail: Initially, the test will fail because the function doesn't exist yet.
Write the Code: Implement the function to make the test pass.
Run the Test and See it Pass: Verify that your implementation works as expected.
Refactor: Clean up your code, ensuring it's well-structured and readable.


Test Class: TestAdditionFunction inherits from unittest.TestCase and tests the add function.
Test Methods: test_addition checks several scenarios:
Adding 5 and 3 should give 8.
Adding -1 and 1 should give 0.
Adding 0 and 0 should give 0.
Implementation: The add function simply returns the sum of two numbers.
Run Tests: The tests are run with unittest.main().
'''
import unittest

# Step 1: Write the Test
class TestAdditionFunction(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(add(5, 3), 8)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

# Step 2: Run the Test to see it fail (Function 'add' not implemented)

# Step 3: Write the Code to make the test pass
def add(x, y):
    return x + y

# Step 4: Run the Test again to see it pass
# Step 5: Refactor if necessary

# Running the tests
if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)


# Another Example
import unittest

# Step 1: Write the Test
class TestFactorialFunction(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(0), 1)
        self.assertRaises(ValueError, factorial, -1)

# Step 2: Run the Test to see it fail (Function 'factorial' not implemented)

# Step 3: Write the Code to make the test pass
def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0:
        return 1
    return n * factorial(n - 1)

# Step 4: Run the Test again to see it pass
# Step 5: Refactor if necessary

# Running the tests
if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)

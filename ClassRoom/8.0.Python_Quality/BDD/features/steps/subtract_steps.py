from programs.calculator import Calculator
from behave import *

@given('a calculator for subtraction')
def step_given_calculator(context):
    context.calculator = Calculator()

@when('I subtract {num1:d} from {num2:d}')
def step_when_subtract_numbers(context, num1, num2):
    context.result = context.calculator.subtract(num2, num1)

@then('the result should be {expected_result:d}')
def step_then_verify_result(context, expected_result):
    assert context.result == expected_result
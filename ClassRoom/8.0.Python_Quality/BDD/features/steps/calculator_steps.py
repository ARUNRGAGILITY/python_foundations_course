from behave import *
from programs.calculator import Calculator

@given('a calculator for addition')
def step_given_calculator(context):
    context.calculator = Calculator()

@when('I add {num1:d} and {num2:d}')
def step_when_add_numbers(context, num1, num2):
    context.result = context.calculator.add(num1, num2)

@then('the result should be {expected_result:d}')
def step_then_verify_result(context, expected_result):
    assert context.result == expected_result
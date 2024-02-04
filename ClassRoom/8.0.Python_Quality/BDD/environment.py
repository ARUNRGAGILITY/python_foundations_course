# environment.py

from programs.calculator import Calculator

def before_all(context):
    # Initialize the Calculator instance
    context.calculator = Calculator()

def after_all(context):
    # Clean up resources if needed
    pass
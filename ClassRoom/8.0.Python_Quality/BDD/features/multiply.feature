Feature: Calculator

  Scenario: Multiply two numbers
    Given a calculator
    When I multiply 6 by 9
    Then the result should be 54
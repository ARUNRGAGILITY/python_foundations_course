Feature: Calculator

  Scenario: Subtract two numbers
    Given a calculator
    When I subtract 7 from 15
    Then the result should be 8
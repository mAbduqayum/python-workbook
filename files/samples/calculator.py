# Calculator Module
# Author: Student
# Date: 2024-01-15


def add(a, b):
    # Add two numbers
    return a + b


def subtract(a, b):
    return a - b  # inline comment stays


# Multiply function
def multiply(a, b):
    return a * b


def divide(a, b):
    # Check for division by zero
    if b == 0:
        return None
    return a / b


# TODO: Add more functions
# FIXME: Handle edge cases


class Calculator:
    # A simple calculator class

    def __init__(self):
        self.result = 0

    def calculate(self, operation, a, b):
        # Perform the calculation
        if operation == "add":
            self.result = add(a, b)
        return self.result

# Functions in Python

## Introduction

Functions are reusable blocks of code that perform specific tasks. They are fundamental building blocks in Python programming that help you:

- **Avoid repetition**: Write code once, use it many times
- **Organize code**: Break complex problems into smaller, manageable pieces
- **Test easily**: Test individual functions independently
- **Improve readability**: Give meaningful names to operations
- **Maintain code**: Fix bugs in one place instead of many

Think of functions as mini-programs within your program. Just like you wouldn't want to rewrite the same paragraph in an essay multiple times, you don't want to repeat the same code throughout your program.

## Function Basics

### Defining a Function

Use the `def` keyword to define a function:

```python
def greet():
    print("Hello, World!")
```

Components:
- `def` - keyword that starts a function definition
- `greet` - function name (follows variable naming rules)
- `()` - parentheses for parameters (empty here)
- `:` - colon to end the function header
- Indented block - the function body

### Calling a Function

To execute a function, use its name followed by parentheses:

```python
def greet():
    print("Hello, World!")

# Call the function
greet()  # Output: Hello, World!
greet()  # Output: Hello, World!
```

You can call a function as many times as needed.

## Parameters and Arguments

Functions become more powerful when they accept input values.

### Single Parameter

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")  # Output: Hello, Alice!
greet("Bob")    # Output: Hello, Bob!
```

- **Parameter**: Variable in the function definition (`name`)
- **Argument**: Actual value passed to the function (`"Alice"`, `"Bob"`)

### Multiple Parameters

```python
def area(length, width):
    a = length * width
    print(f"Area: {a}")

area(5, 3)   # Output: Area: 15
area(10, 4)  # Output: Area: 40
```

### Default Parameter Values

Parameters can have default values:

```python
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alice")              # Output: Hello, Alice!
greet("Bob", "Hi")          # Output: Hi, Bob!
greet("Charlie", "Hey")     # Output: Hey, Charlie!
```

Default parameters must come after non-default parameters.

## Return Values

Functions can return values using the `return` statement.

### Single Return Value

```python
def add(a, b):
    return a + b

result = add(3, 5)
print(result)  # Output: 8

# Use directly in expressions
total = add(10, 20) + add(5, 3)
print(total)  # Output: 38
```

### Return vs Print

**Important distinction:**

```python
# This function PRINTS but doesn't return
def add_and_print(a, b):
    print(a + b)

# This function RETURNS a value
def add_and_return(a, b):
    return a + b

# Comparison
result1 = add_and_print(3, 5)   # Prints: 8
print(result1)                  # Prints: None (no return value)

result2 = add_and_return(3, 5)  # No output
print(result2)                  # Prints: 8
```

**Key difference**:
- `print()` displays output to the user
- `return` provides a value that can be used in your code

### Functions Without Return

If a function doesn't have a `return` statement, it returns `None`:

```python
def greet(name):
    print(f"Hello, {name}!")

result = greet("Alice")  # Prints: Hello, Alice!
print(result)            # Prints: None
```

### Multiple Return Values

Functions can return multiple values as a tuple:

```python
def calculate_circle(radius):
    import math
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area, circumference

# Unpack the return values
area, circ = calculate_circle(5)
print(f"Area: {area:.2f}")              # Area: 78.54
print(f"Circumference: {circ:.2f}")     # Circumference: 31.42

# Or get as a tuple
result = calculate_circle(3)
print(result)  # (28.274..., 18.849...)
```

### Early Return

You can return early from a function:

```python
def is_even(number):
    if number % 2 == 0:
        return True
    return False

# More concise version
def is_even(number):
    return number % 2 == 0

print(is_even(4))  # True
print(is_even(7))  # False
```

## Type Hints

Type hints make code more readable and help catch errors. They don't affect how Python runs your code but provide documentation and enable better tooling support.

### Basic Type Hints

```python
def add(a: int, b: int) -> int:
    return a + b

def greet(name: str) -> None:
    print(f"Hello, {name}!")

def calculate_average(numbers: list) -> float:
    return sum(numbers) / len(numbers)
```

Syntax:
- `parameter: type` - parameter type hint
- `-> type` - return type hint
- `-> None` - function doesn't return a value

### Common Type Hints

```python
def process_age(age: int) -> str:
    return f"Age: {age}"

def calculate_area(length: float, width: float) -> float:
    return length * width

def is_valid(value: bool) -> bool:
    return not value

def get_items(data: list) -> tuple:
    return (data[0], data[-1])
```

### Why Use Type Hints?

1. **Documentation**: Makes function expectations clear
2. **IDE Support**: Better autocomplete and error detection
3. **Readability**: Easier to understand what a function expects
4. **Debugging**: Catch type errors early with tools like mypy

```python
# Clear expectations
def calculate_bmi(weight_kg: float, height_m: float) -> float:
    return weight_kg / (height_m ** 2)

# Without type hints - less clear
def calculate_bmi(weight, height):
    return weight / (height ** 2)
```

## Docstrings

Docstrings document what a function does. They appear as the first statement in a function.

### Single-Line Docstring

```python
def square(x: int) -> int:
    """Return the square of x."""
    return x * x
```

### Multi-Line Docstring

```python
def calculate_bmi(weight_kg: float, height_m: float) -> float:
    """
    Calculate Body Mass Index (BMI).

    Parameters:
        weight_kg: Weight in kilograms
        height_m: Height in meters

    Returns:
        BMI value as a float
    """
    return weight_kg / (height_m ** 2)
```

### Accessing Docstrings

```python
print(calculate_bmi.__doc__)
# Or use help()
help(calculate_bmi)
```

## Function Scope

Variables created inside a function are **local** to that function.

### Local Variables

```python
def calculate():
    x = 10  # Local variable
    return x * 2

result = calculate()
print(result)  # 20
# print(x)  # Error: x is not defined
```

### Global Variables

Variables defined outside functions are global:

```python
total = 0  # Global variable

def add_to_total(value):
    global total
    total += value

add_to_total(5)
add_to_total(3)
print(total)  # 8
```

**Best Practice**: Avoid using `global`. Instead, pass values as parameters and return results.

### Parameters Create Local Variables

```python
def greet(name):  # name is a local variable
    message = f"Hello, {name}!"  # the message is also local
    return message

print(greet("Alice"))
# print(name)  # Error: name is not defined
```

### Shadowing Global Variables

Local variables can have the same name as global variables:

```python
x = 100  # Global

def calculate():
    x = 10  # Local (different from global x)
    return x * 2

print(calculate())  # 20
print(x)            # 100 (global unchanged)
```

## Common Patterns

### Mathematical Calculations

```python
import math

def calculate_circle_area(radius: float) -> float:
    """Calculate the area of a circle."""
    return math.pi * radius ** 2

def calculate_hypotenuse(a: float, b: float) -> float:
    """Calculate hypotenuse using Pythagorean theorem."""
    return math.sqrt(a ** 2 + b ** 2)

print(calculate_circle_area(5))     # 78.54...
print(calculate_hypotenuse(3, 4))   # 5.0
```

### Boolean-Returning Functions

Functions that return `True` or `False` often start with "is" or "has":

```python
def is_even(number: int) -> bool:
    """Check if a number is even."""
    return number % 2 == 0

def is_prime(n: int) -> bool:
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_palindrome(text: str) -> bool:
    """Check if the text is a palindrome."""
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]

print(is_even(4))              # True
print(is_prime(17))            # True
print(is_palindrome("radar"))  # True
```

### Conversion Functions

```python
def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5 / 9

def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert Celsius to Fahrenheit."""
    return celsius * 9 / 5 + 32

def binary_to_decimal(binary: str) -> int:
    """Convert binary string to decimal integer."""
    return int(binary, 2)

print(fahrenheit_to_celsius(98.6))    # 37.0
print(celsius_to_fahrenheit(100))     # 212.0
print(binary_to_decimal("1010"))      # 10
```

### String Manipulation

```python
def caesar_cipher(text: str, shift: int) -> str:
    """Encrypt text using Caesar cipher."""
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - start + shift) % 26
            result += chr(start + shifted)
        else:
            result += char
    return result

def count_vowels(text: str) -> int:
    """Count vowels in text."""
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)

print(caesar_cipher("HELLO", 3))   # KHOOR
print(count_vowels("Hello World"))  # 3
```

### Accumulation Pattern

```python
def sum_of_digits(number: int) -> int:
    """Calculate the sum of digits in a number."""
    total = 0
    number = abs(number)  # Handle negative numbers
    while number > 0:
        total += number % 10
        number //= 10
    return total

def factorial(n: int) -> int:
    """Calculate factorial of n."""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(sum_of_digits(12345))  # 15
print(factorial(5))          # 120
```

### Validation Pattern

```python
def is_valid_triangle(a: float, b: float, c: float) -> bool:
    """Check if three sides can form a valid triangle."""
    return (a + b > c) and (a + c > b) and (b + c > a)

def is_leap_year(year: int) -> bool:
    """Check if a year is a leap year."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

print(is_valid_triangle(3, 4, 5))  # True
print(is_valid_triangle(1, 1, 10)) # False
print(is_leap_year(2024))          # True
print(is_leap_year(2023))          # False
```

## Best Practices

### 1. Function Naming

Use descriptive names that indicate what the function does:

```python
# Good
def calculate_area(length, width):
    return length * width

def is_valid_email(email):
    return "@" in email

# Poor
def calc(l, w):
    return l * w

def check(e):
    return "@" in e
```

**Naming conventions:**
- Use lowercase with underscores: `calculate_area`
- Start boolean functions with `is_`, `has_`, `can_`: `is_even`, `has_permission`
- Use verbs for actions: `calculate`, `convert`, `validate`
- Be specific: `get_user_age` not just `get_data`

### 2. Single Responsibility

Each function should do one thing well:

```python
# Good - each function has one responsibility
def get_radius():
    return float(input("Enter radius: "))

def calculate_area(radius):
    import math
    return math.pi * radius ** 2

def display_result(area):
    print(f"Area: {area:.2f}")

# Usage
radius = get_radius()
area = calculate_area(radius)
display_result(area)

# Poor - one function does everything
def do_everything():
    radius = float(input("Enter radius: "))
    import math
    area = math.pi * radius ** 2
    print(f"Area: {area:.2f}")
```

### 3. Keep Functions Short

Aim for functions that fit on one screen (typically 10-20 lines):

```python
# Good - broken into smaller functions
def is_strong_password(password):
    return (has_minimum_length(password) and
            has_uppercase(password) and
            has_digit(password))

def has_minimum_length(password):
    return len(password) >= 8

def has_uppercase(password):
    return any(c.isupper() for c in password)

def has_digit(password):
    return any(c.isdigit() for c in password)
```

### 4. Avoid Side Effects

Functions should avoid changing the global state:

```python
# Good - pure function (no side effects)
def add(a, b):
    return a + b

# Poor - modifies global variable
total = 0
def add_to_total(value):
    global total
    total += value
```

### 5. Use Type Hints

Make your function expectations clear:

```python
# Good - clear expectations
def calculate_discount(price: float, discount_percent: float) -> float:
    return price * (1 - discount_percent / 100)

# Less clear
def calculate_discount(price, discount):
    return price * (1 - discount / 100)
```

### 6. Document Complex Functions

Use docstrings for non-trivial functions:

```python
def normalize_fraction(numerator: int, denominator: int) -> tuple:
    """
    Reduce a fraction to its simplest form.

    Parameters:
        numerator: The top number of the fraction
        denominator: The bottom number of the fraction

    Returns:
        A tuple (num, denom) in the simplest form

    Example:
        normalize_fraction(6, 9) returns (2, 3)
    """
    import math
    gcd = math.gcd(numerator, denominator)
    return numerator // gcd, denominator // gcd
```

### 7. Return Early for Validation

Handle edge cases early with early returns:

```python
# Good - early return
def divide(a, b):
    if b == 0:
        return None  # or raise an exception
    return a / b

# Poor - nested conditions
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return None
```

## When to Create a Function

Create a function when:

1. **You repeat code** - If you're copying and pasting code, make it a function
2. **Code is complex** - Break complex logic into named functions
3. **You need to test** - Functions make testing easier
4. **Code has a clear purpose** - Any operation with a clear purpose deserves a function
5. **You want to reuse logic** - Functions enable reusability

```python
# Without functions - repetitive
radius1 = 5
area1 = 3.14159 * radius1 ** 2
print(f"Circle 1 area: {area1}")

radius2 = 10
area2 = 3.14159 * radius2 ** 2
print(f"Circle 2 area: {area2}")

# With function - reusable and clear
import math

def calculate_circle_area(radius: float) -> float:
    return math.pi * radius ** 2

print(f"Circle 1 area: {calculate_circle_area(5)}")
print(f"Circle 2 area: {calculate_circle_area(10)}")
```

## Quick Reference

| Concept | Syntax | Example |
|---------|--------|---------|
| Define function | `def name():` | `def greet():` |
| With parameters | `def name(param):` | `def greet(name):` |
| With return | `def name(): return value` | `def add(a, b): return a + b` |
| Default parameter | `def name(param=default):` | `def greet(name="World"):` |
| Type hints | `def name(p: type) -> type:` | `def add(a: int, b: int) -> int:` |
| Call function | `name()` | `greet()` |
| Call with args | `name(arg1, arg2)` | `add(3, 5)` |
| Multiple returns | `return val1, val2` | `return area, perimeter` |
| Unpack returns | `a, b = function()` | `area, perim = calculate()` |
| Docstring | `"""Description"""` | `"""Calculate sum."""` |
| Local variable | Variable inside function | `x = 10` in function |
| Global access | `global var_name` | `global counter` |

## Summary

**Key Concepts:**

1. **Functions** group related code into reusable blocks
2. **Parameters** let functions accept input values
3. **Return values** let functions provide output
4. **Type hints** document expected types
5. **Docstrings** explain what functions do
6. **Local scope** means variables in functions are isolated
7. **Best practices** include clear naming, single responsibility, and avoiding side effects

**Remember:**
- Use `return` to provide values, `print()` to show output
- Keep functions focused on one task
- Use descriptive names that explain what the function does
- Add type hints for clarity
- Functions make code more maintainable and testable

Functions are essential for writing clean, organized, and professional Python code!

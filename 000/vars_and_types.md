# Variables and Data Types - Essential Concepts

This guide covers all the fundamental concepts you need to solve exercises.

## 1. Variables

Variables are containers that store data values. In Python, you create a variable by assigning a value to it.

```python
# Creating variables
name = "Alice"
age = 25
price = 12.99
```

**Rules for variable names:**
- Must start with a letter or underscore
- Can contain letters, numbers, and underscores
- Case-sensitive (`age` and `Age` are different)
- Cannot use Python keywords (`print`, `input`, `if`, etc.)

## 2. Data Types

### Strings (str)
Text data enclosed in quotes.
```python
message = "Hello, World!"
name = 'John'
```

### Integers (int)
Whole numbers without decimal points.
```python
age = 25
count = 0
year = 2024
```

### Floating-point numbers (float)
Numbers with decimal points.
```python
price = 19.99
temperature = 25.5
pi = 3.14159
```

## 3. Input and Output

### Getting input from users
```python
name = input("Enter your name: ")  # Always returns a string
age_str = input("Enter your age: ")  # This is a string, not a number
```

### Displaying output
```python
print("Hello, World!")              # Simple text
print("Your age is:", age)          # Multiple items
print(f"Hello {name}")              # f-string formatting
```

## 4. Type Conversion

Since `input()` always returns a string, you often need to convert it to numbers.

```python
# Converting strings to numbers
age_str = input("Enter age: ")
age = int(age_str)                  # Convert to integer

price_str = input("Enter price: ")
price = float(price_str)            # Convert to float

# You can do it in one line
age = int(input("Enter age: "))
price = float(input("Enter price: "))
```

## 5. Arithmetic Operations

### Basic operators
```python
a = 10
b = 3

addition = a + b        # 13
subtraction = a - b     # 7
multiplication = a * b  # 30
division = a / b        # 3.333...
```

### Advanced operators
```python
floor_division = a // b # 3 (integer division)
modulo = a % b          # 1 (remainder)
exponentiation = a ** b # 1000 (10 to the power of 3)
```

## 6. Working with Numbers

### Common calculations
```python
# Rectangle area
length = 5
width = 3
area = length * width

# Circle area
radius = 4
pi = 3.14159
area = pi * radius ** 2

# Average of three numbers
num1 = 10
num2 = 20  
num3 = 30
average = (num1 + num2 + num3) / 3
```

### Temperature conversion
```python
celsius = 25
fahrenheit = (celsius * 9/5) + 32
```

### Time conversion
```python
total_seconds = 125
minutes = total_seconds // 60    # 2
remaining_seconds = total_seconds % 60  # 5
```

## 7. String Formatting and Operations

**For detailed string formatting patterns and examples, see: `000/string_formatting.md`**

### Basic string operations
```python
# Simple concatenation
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name

# Using print() with multiple values
name = "Alice"
age = 25
print("Hello", name, "you are", age, "years old")
```

### f-strings (RECOMMENDED)
```python
name = "Alice"
age = 25
print(f"Hello {name}, you are {age} years old")
print(f"The area is: {area:.2f}")  # 2 decimal places
```

### String methods (useful to know)
```python
text = "Hello World"
print(text.upper())         # HELLO WORLD
print(text.lower())         # hello world
print(len(text))            # 11
```

## 8. Comments

Use comments to explain your code:
```python
# This is a single-line comment
name = input("Enter your name: ")  # Get user's name
```

## 9. Program Structure

A typical program follows this pattern:
```python
# 1. Get input from user
radius = float(input("Enter radius: "))

# 2. Perform calculations
pi = 3.14159
area = pi * radius ** 2

# 3. Display results
print(f"The area is: {area}")
```

## 10. Common Patterns for Exercises

### Pattern 1: Simple calculation
```python
# Get two numbers and calculate their sum
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
sum_result = num1 + num2
print(f"The sum is: {sum_result}")
```

### Pattern 2: Formula application
```python
# Calculate rectangle area
length = float(input("Enter length: "))
width = float(input("Enter width: "))
area = length * width
print(f"The area is: {area}")
```

### Pattern 3: Unit conversion
```python
# Convert seconds to minutes and seconds
total_seconds = int(input("Enter seconds: "))
minutes = total_seconds // 60
seconds = total_seconds % 60
print(f"{total_seconds} seconds = {minutes} minutes and {seconds} seconds")
```

## 11. Tips for Success

1. **Always convert input to the right type:**
   ```python
   # Wrong: age = input("Enter age: ")  # This is a string!
   # Right: age = int(input("Enter age: "))
   ```

2. **Use descriptive variable names:**
   ```python
   # Wrong: x = 5, y = 3, z = x * y
   # Right: length = 5, width = 3, area = length * width
   ```

3. **Pay attention to output formatting:**
   ```python
    # If exercise asks for "The result is: 42"
    print(f"The result is: {result}")  # Exact format matters
   ```

4. **Test with the example data:**
   - Run your program with the exact input from the exercise
   - Check that output matches exactly

5. **Common mistakes to avoid:**
   - Forgetting to convert strings to numbers
   - Using wrong data types (int vs float)
   - Incorrect output formatting
   - Wrong arithmetic operations

## Quick Reference

| Operation         | Example                           | Result  |
|-------------------|-----------------------------------|---------|
| Get string input  | `name = input("Name: ")`          | String  |
| Get integer input | `age = int(input("Age: "))`       | Integer |
| Get float input   | `price = float(input("Price: "))` | Float   |
| Addition          | `5 + 3`                           | 8       |
| Subtraction       | `5 - 3`                           | 2       |
| Multiplication    | `5 * 3`                           | 15      |
| Division          | `5 / 3`                           | 1.667   |
| Integer division  | `5 // 3`                          | 1       |
| Remainder         | `5 % 3`                           | 2       |
| Power             | `5 ** 3`                          | 125     |
| Print simple      | `print("Hello")`                  | Hello   |
| Print variable    | `print(f"Age: {age}")`            | Age: 25 |

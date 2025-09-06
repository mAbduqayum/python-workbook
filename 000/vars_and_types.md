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

### Method 1: String concatenation with +
```python
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name

name = "Alice"
age = 25
message = "Hello " + name + ", you are " + str(age) + " years old"
```

**Note:** You must convert numbers to strings using `str()` when concatenating.

### Method 2: Using commas in print()
```python
name = "Alice"
age = 25
print("Hello", name, "you are", age, "years old")
# Output: Hello Alice you are 25 years old
```

### Method 3: f-strings (Formatted String Literals) - RECOMMENDED
f-strings are the most modern and readable way to format strings in Python.

```python
name = "Alice"
age = 25
score = 85.67

# Basic f-string usage
greeting = f"Hello {name}!"
message = f"You are {age} years old"

# With calculations inside
radius = 5
area = f"Area is: {3.14159 * radius ** 2}"

# Multiple variables
result = f"Hello {name}, your score is {score}"
```

### Method 4: .format() method
```python
name = "Alice"
age = 25
message = "Hello {}, you are {} years old".format(name, age)

# With named placeholders
message = "Hello {name}, you are {age} years old".format(name=name, age=age)
```

### Method 5: % formatting (older style)
```python
name = "Alice"
age = 25
message = "Hello %s, you are %d years old" % (name, age)
```

### String formatting for numbers

#### Controlling decimal places
```python
pi = 3.14159265
price = 19.99

# 2 decimal places
print(f"Pi is approximately: {pi:.2f}")        # Pi is approximately: 3.14
print(f"Price: ${price:.2f}")                  # Price: $19.99

# No decimal places (rounded)
print(f"Pi rounded: {pi:.0f}")                 # Pi rounded: 3
```

#### Formatting integers
```python
number = 42
large_number = 1234567

# Basic integer
print(f"The answer is: {number}")              # The answer is: 42

# With width (padding)
print(f"Number: {number:5d}")                  # Number:    42 (5 characters wide)
print(f"Number: {number:05d}")                 # Number: 00042 (padded with zeros)

# With thousands separator
print(f"Large number: {large_number:,}")       # Large number: 1,234,567
```

#### Common formatting patterns for exercises
```python
# Exercise output patterns
name = "John"
result = 42.5
num1 = 15
num2 = 27

# Pattern 1: "Hello [name]!"
print(f"Hello {name}!")

# Pattern 2: "The result is: [number]"
print(f"The result is: {result}")

# Pattern 3: "The sum is: [number]"
total = num1 + num2
print(f"The sum is: {total}")

# Pattern 4: Multiple values
total_seconds = 125
minutes = 2
seconds = 5
print(f"{total_seconds} seconds = {minutes} minutes and {seconds} seconds")
```

### String methods (useful to know)
```python
text = "Hello World"

# Case methods
print(text.upper())         # HELLO WORLD
print(text.lower())         # hello world
print(text.title())         # Hello World

# Length
print(len(text))            # 11

# Replace
print(text.replace("World", "Python"))  # Hello Python
```

### Escape characters
```python
# Special characters in strings
quote = "She said \"Hello\" to me"        # Using \" for quotes inside string
path = "C:\\Users\\Documents"             # Using \\ for backslash
newline = "Line 1\nLine 2"                # Using \n for new line
tab = "Column1\tColumn2"                  # Using \t for tab
```

### Best practices for string formatting

1. **Use f-strings for most cases (Python 3.6+):**
   ```python
   # Good
   print(f"Hello {name}, your age is {age}")
   
   # Avoid (harder to read)
   print("Hello " + name + ", your age is " + str(age))
   ```

2. **Match exact output format required:**
   ```python
   # If exercise asks for: "The area is: 15"
   area = 15
   print(f"The area is: {area}")  # Exact spacing and punctuation
   ```

3. **Use appropriate number formatting:**
   ```python
   # For money
   price = 19.99
   print(f"Price: ${price:.2f}")
   
   # For percentages
   rate = 0.15
   print(f"Rate: {rate:.1%}")      # Rate: 15.0%
   ```

4. **Common formatting mistakes to avoid:**
   ```python
   # Wrong - extra spaces
   print(f"Result : {result}")
   
   # Right - match the required format exactly  
   print(f"Result: {result}")
   
   # Wrong - converting when not needed
   age = 25
   print("Age: " + str(age))
   
   # Right - use f-string
   print(f"Age: {age}")
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

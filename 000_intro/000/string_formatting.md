# F-String Formatting Reference

Complete guide to Python f-string formatting with all syntax options and examples.

## Basic F-String Syntax

```python
name = "Alice"
age = 25
print(f"Hello {name}, you are {age} years old")
# Output: Hello Alice, you are 25 years old
```

## Format Specifier Syntax

```
f"{value:format_spec}"
```

Where `format_spec` follows the pattern: `[[fill]align][sign][#][0][width][grouping_option][.precision][type]`

## Number Formatting

### Integer Formatting

| Specifier | Description | Example | Output |
|-----------|-------------|---------|--------|
| `{n:d}` | Decimal integer | `f"{42:d}"` | 42 |
| `{n:b}` | Binary | `f"{42:b}"` | 101010 |
| `{n:o}` | Octal | `f"{42:o}"` | 52 |
| `{n:x}` | Hexadecimal (lowercase) | `f"{42:x}"` | 2a |
| `{n:X}` | Hexadecimal (uppercase) | `f"{42:X}"` | 2A |
| `{n:c}` | Character | `f"{65:c}"` | A |

### Float Formatting

| Specifier | Description | Example | Output |
|-----------|-------------|---------|--------|
| `{n:f}` | Fixed-point | `f"{3.14159:f}"` | 3.141590 |
| `{n:.2f}` | 2 decimal places | `f"{3.14159:.2f}"` | 3.14 |
| `{n:.0f}` | No decimal places | `f"{3.14159:.0f}"` | 3 |
| `{n:e}` | Scientific (lowercase) | `f"{1234.5:e}"` | 1.234500e+03 |
| `{n:E}` | Scientific (uppercase) | `f"{1234.5:E}"` | 1.234500E+03 |
| `{n:.2e}` | Scientific with precision | `f"{1234.5:.2e}"` | 1.23e+03 |
| `{n:g}` | General format | `f"{1234.5:g}"` | 1234.5 |
| `{n:%}` | Percentage | `f"{0.1234:%}"` | 12.340000% |
| `{n:.2%}` | Percentage with precision | `f"{0.1234:.2%}"` | 12.34% |

## Width and Alignment

### Width Specification

| Format | Description | Example | Output |
|--------|-------------|---------|--------|
| `{n:5}` | Minimum width 5 | `f"{42:5}"` | "   42" |
| `{n:05}` | Width 5, zero-padded | `f"{42:05}"` | "00042" |
| `{s:10}` | String width 10 | `f"{'hello':10}"` | "hello     " |

### Alignment Options

| Align | Description | Example | Output |
|-------|-------------|---------|--------|
| `<` | Left align | `f"{'hello':<10}"` | "hello     " |
| `>` | Right align | `f"{'hello':>10}"` | "     hello" |
| `^` | Center align | `f"{'hello':^10}"` | "  hello   " |
| `=` | Sign-aware padding | `f"{-42:=5}"` | "-  42" |

### Custom Fill Characters

```python
value = 42
print(f"{value:*<5}")   # 42***
print(f"{value:*>5}")   # ***42  
print(f"{value:*^5}")   # *42**
print(f"{value:*=5}")   # ***42 (numbers only)
```

## Sign Handling

| Sign | Description | Example | Output |
|------|-------------|---------|--------|
| `+` | Show sign always | `f"{42:+}"` | +42 |
| `-` | Show sign for negatives only (default) | `f"{42:-}"` | 42 |
| ` ` (space) | Space for positive, minus for negative | `f"{42: }"` | " 42" |

```python
positive = 42
negative = -42
print(f"{positive:+}")  # +42
print(f"{negative:+}")  # -42
print(f"{positive: }")  # " 42" 
print(f"{negative: }")  # "-42"
```

## Grouping and Separators

| Specifier | Description | Example | Output |
|-----------|-------------|---------|--------|
| `,` | Thousands separator | `f"{1234567:,}"` | 1,234,567 |
| `_` | Underscore separator | `f"{1234567:_}"` | 1_234_567 |
| `,.2f` | Float with thousands separator | `f"{1234567.89:,.2f}"` | 1,234,567.89 |

## Alternative Form (#)

```python
number = 42
print(f"{number:#b}")   # 0b101010 (binary with prefix)
print(f"{number:#o}")   # 0o52 (octal with prefix)  
print(f"{number:#x}")   # 0x2a (hex with prefix)

float_num = 3.0
print(f"{float_num:#f}") # 3.000000 (always show decimal point)
```

## String-Specific Formatting

### Case Conversion (using methods inside f-strings)

```python
name = "alice"
print(f"{name.upper()}")     # ALICE
print(f"{name.lower()}")     # alice  
print(f"{name.title()}")     # Alice
print(f"{name.capitalize()}") # Alice
```

### String Truncation and Padding

```python
text = "Hello World"
print(f"{text:.5}")      # Hello (truncate to 5 chars)
print(f"{text:15}")      # "Hello World    " (pad to 15)
print(f"{text:<15}")     # "Hello World    " (left align)
print(f"{text:>15}")     # "    Hello World" (right align)
print(f"{text:^15}")     # "  Hello World  " (center)
```

## Expressions in F-Strings

```python
a = 5
b = 3
print(f"{a} + {b} = {a + b}")           # 5 + 3 = 8
print(f"{a} * {b} = {a * b}")           # 5 * 3 = 15
print(f"Square of {a} is {a**2}")       # Square of 5 is 25

# With formatting
print(f"{a} / {b} = {a/b:.2f}")         # 5 / 3 = 1.67

# Function calls
import math
print(f"Square root of {a} is {math.sqrt(a):.2f}")  # Square root of 5 is 2.24
```

## Nested F-Strings

```python
name = "Alice"
value = 42.12345
precision = 2

# Nested f-string for dynamic precision
print(f"Hello {name}, value is {value:.{precision}f}")  # Hello Alice, value is 42.12

# Dynamic width
width = 10
print(f"{'Hello':{width}}")  # Hello     (padded to 10 chars)
```

## Date and Time Formatting

```python
from datetime import datetime

now = datetime.now()
print(f"{now:%Y-%m-%d}")           # 2024-03-15
print(f"{now:%H:%M:%S}")           # 14:30:25  
print(f"{now:%B %d, %Y}")          # March 15, 2024
print(f"{now:%A, %B %d, %Y}")      # Friday, March 15, 2024
```

## Special Characters and Escaping

```python
# Literal braces
print(f"{{Hello}}")              # {Hello}
print(f"Value: {42} {{units}}")  # Value: 42 {units}

# Quotes inside f-strings
name = "Alice"
print(f'She said "Hello {name}"')     # She said "Hello Alice"  
print(f"He said 'Hello {name}'")      # He said 'Hello Alice'

# Raw strings with f-strings (Python 3.12+)
path = "C:\\Users"
print(rf"{path}\Documents")      # C:\Users\Documents
```

## Debugging with F-Strings (Python 3.8+)

```python
value = 42
result = value * 2

# The = specifier shows both expression and value
print(f"{value=}")              # value=42
print(f"{result=}")             # result=84  
print(f"{value * 3=}")          # value * 3=126

# With formatting
pi = 3.14159
print(f"{pi=:.2f}")             # pi=3.14
```

## Advanced Examples

### Complex Number Formatting

```python
# Multiple values with different formatting
name = "Alice"
score = 87.456
percentage = 0.87456

print(f"Student: {name:<10} Score: {score:6.1f} ({percentage:6.1%})")
# Output: Student: Alice      Score:   87.5 ( 87.5%)
```

### Table Formatting

```python
items = [
    ("Apples", 5, 1.25),
    ("Bananas", 12, 0.75),  
    ("Oranges", 8, 1.50)
]

print(f"{'Item':<10} {'Qty':>5} {'Price':>8}")
print("-" * 25)
for item, qty, price in items:
    print(f"{item:<10} {qty:>5} ${price:>7.2f}")

# Output:
# Item         Qty    Price
# -------------------------
# Apples         5 $   1.25
# Bananas       12 $   0.75
# Oranges        8 $   1.50
```

### Scientific Data

```python
measurements = [1234.567, 0.000456, 987654321.0]

for i, value in enumerate(measurements):
    print(f"Measurement {i+1}:")
    print(f"  Standard: {value:,.2f}")
    print(f"  Scientific: {value:.2e}")
    print(f"  Engineering: {value:.3g}")
    print()

# Output shows different representations of the same numbers
```

## Format Specification Summary

| Component | Options | Purpose |
|-----------|---------|---------|
| **fill** | Any character | Character to use for padding |
| **align** | `<` `>` `^` `=` | Alignment within width |
| **sign** | `+` `-` ` ` | How to display number signs |
| **#** | `#` | Alternate form (0x, 0b, etc.) |
| **0** | `0` | Zero-padding |
| **width** | Integer | Minimum field width |
| **grouping** | `,` `_` | Thousands separator |
| **precision** | `.n` | Decimal places or significant digits |
| **type** | `d` `f` `e` `s` etc. | Format type |

This reference covers the complete f-string formatting syntax available in Python, from basic variable insertion to advanced formatting options for numbers, strings, dates, and complex layouts.

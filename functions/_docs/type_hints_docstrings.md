# Functions in Python - Type Hints and Docstrings

## Type Hints

Type hints make code more readable and help catch errors. They don't affect how Python runs your code but provide documentation and enable better tooling support.

### Basic Type Hints

```python
def add(a: int, b: int) -> int:
    return a + b

def greet(name: str) -> None:
    print(f"Hello, {name}!")

def average(a: float, b: float) -> float:
    return (a + b) / 2
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

def is_adult(age: int) -> bool:
    return age >= 18

def full_name(first: str, last: str) -> str:
    return first + " " + last
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

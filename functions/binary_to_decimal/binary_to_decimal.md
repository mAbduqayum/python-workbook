# Binary to Decimal

Write a function that converts a binary string to decimal.

## Task
- Create a function `binary_to_decimal(binary)` that takes a binary string
- Assume the input contains only `0` and `1`
- Return the decimal (base 10) equivalent
- Don't use the built-in `int(binary, 2)`

## Template:
```python
def binary_to_decimal(binary: str) -> int:
    pass


if __name__ == "__main__":
    # Test your function
    print(binary_to_decimal("1010"))      # 10
    print(binary_to_decimal("1111"))      # 15
    print(binary_to_decimal("0"))         # 0
    print(binary_to_decimal("1"))         # 1
    print(binary_to_decimal("10000"))     # 16
```


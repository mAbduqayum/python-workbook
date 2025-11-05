# Binary to Decimal

Write a function that converts a binary string to decimal.

## Task
- Create a function `binary_to_decimal(binary)` that takes a binary string
- Return the decimal (base 10) equivalent

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

## Logic
- Process each bit from right to left
- Each bit position represents a power of 2
- Multiply bit value by 2^position and sum

## Note
- Don't use built-in `int(binary, 2)`
- Implement the conversion algorithm manually
- Assume valid binary input (only '0' and '1')

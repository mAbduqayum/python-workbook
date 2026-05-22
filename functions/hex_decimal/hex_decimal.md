# Hexadecimal to Decimal

Write a function that converts a hexadecimal string to decimal.

## Task
- Create a function `hex_decimal(hex_str)` that takes a hexadecimal string
- Return the decimal (base 10) equivalent

## Template:
```python
def hex_decimal(hex_str: str) -> int:
    pass


if __name__ == "__main__":
    # Test your function
    print(hex_decimal("A"))       # 10
    print(hex_decimal("FF"))      # 255
    print(hex_decimal("10"))      # 16
    print(hex_decimal("1A"))      # 26
    print(hex_decimal("ABC"))     # 2748
```

## Note
- Don't use the built-in `int(hex_str, 16)`
- Accept both uppercase and lowercase letters

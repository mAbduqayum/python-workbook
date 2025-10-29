# Hexadecimal to Decimal

Write a function that converts a hexadecimal string to decimal.

## Task
- Create a function `hex_decimal(hex_str)` that takes a hexadecimal string
- Return the decimal (base 10) equivalent

## Function Signature
```python
def hex_decimal(hex_str: str) -> int:
    pass
```

## Examples
```python
hex_decimal("A")       # 10
hex_decimal("FF")      # 255
hex_decimal("10")      # 16
hex_decimal("1A")      # 26
hex_decimal("ABC")     # 2748
```

## Logic
- Hexadecimal uses digits 0-9 and letters A-F (representing 10-15)
- Each position represents a power of 16
- Process from right to left

## Note
- Don't use built-in `int(hex_str, 16)`
- Implement the conversion algorithm manually
- Handle both uppercase and lowercase letters
- Map A-F (or a-f) to 10-15

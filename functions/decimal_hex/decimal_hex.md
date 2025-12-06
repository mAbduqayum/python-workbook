# Decimal to Hexadecimal

Write a function that converts a decimal number to hexadecimal string.

## Task
- Create a function `decimal_hex(n)` that takes a decimal integer
- Return the hexadecimal representation as a string

## Template:
```python
def decimal_hex(n: int) -> str:
    pass


if __name__ == "__main__":
    # Test your function
    print(decimal_hex(10))       # "A"
    print(decimal_hex(255))      # "FF"
    print(decimal_hex(16))       # "10"
    print(decimal_hex(26))       # "1A"
    print(decimal_hex(0))        # "0"
```

## Logic
- Repeatedly divide by 16 and collect remainders
- Map remainders 0-9 to digits '0'-'9'
- Map remainders 10-15 to letters 'A'-'F'
- Remainders form the hex digits in reverse order

## Note
- Don't use built-in `hex()`
- Implement the conversion algorithm manually
- Use uppercase letters (A-F)
- Return a string

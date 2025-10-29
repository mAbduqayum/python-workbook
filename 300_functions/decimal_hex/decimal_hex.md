# Decimal to Hexadecimal

Write a function that converts a decimal number to hexadecimal string.

## Task
- Create a function `decimal_hex(n)` that takes a decimal integer
- Return the hexadecimal representation as a string

## Function Signature
```python
def decimal_hex(n: int) -> str:
    pass
```

## Examples
```python
decimal_hex(10)       # "A"
decimal_hex(255)      # "FF"
decimal_hex(16)       # "10"
decimal_hex(26)       # "1A"
decimal_hex(0)        # "0"
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

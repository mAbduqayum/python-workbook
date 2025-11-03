# Decimal to Binary

Write a function that converts a decimal number to binary string.

## Task
- Create a function `decimal_to_binary(n)` that takes a decimal integer
- Return the binary representation as a string

## Template:
```python
def decimal_to_binary(n: int) -> str:
    pass


if __name__ == "__main__":
    # Test your function
    decimal_to_binary(10)      # "1010"
    decimal_to_binary(15)      # "1111"
    decimal_to_binary(0)       # "0"
    decimal_to_binary(1)       # "1"
    decimal_to_binary(16)      # "10000"
```

## Logic
- Repeatedly divide by 2 and collect remainders
- Remainders form the binary digits in reverse order
- Special case: 0 returns "0"

## Note
- Don't use built-in `bin()`
- Implement the conversion algorithm manually
- Return a string, not an integer

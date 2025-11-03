# Convert to Any Base

Write a function that converts a decimal number to any base (2-36).

## Task
- Create a function `to_base(n, base)` that takes a decimal integer and target base
- Return the representation in the target base as a string

## Template:
```python
def to_base(n: int, base: int) -> str:
    pass


if __name__ == "__main__":
    # Test your function
    to_base(10, 2)       # "1010"
    to_base(255, 16)     # "FF"
    to_base(8, 8)        # "10"
    to_base(100, 5)      # "400"
    to_base(0, 10)       # "0"
```

## Logic
- Similar to decimal to binary/hex conversions
- Use digits 0-9 and letters A-Z for bases up to 36
- Repeatedly divide by base and collect remainders
- Map remainders to appropriate characters

## Note
- Base should be between 2 and 36 inclusive
- Use uppercase letters for digits > 9
- Return a string
- Handle special case for 0

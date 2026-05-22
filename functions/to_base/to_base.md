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
    print(to_base(10, 2))       # "1010"
    print(to_base(255, 16))     # "FF"
    print(to_base(8, 8))        # "10"
    print(to_base(100, 5))      # "400"
    print(to_base(0, 10))       # "0"
```

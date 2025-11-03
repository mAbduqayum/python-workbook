# Is Even

Write a function that determines if a number is even.

## Task
- Create a function `is_even(n)` that takes an integer
- Return `True` if the number is even, `False` otherwise

## Template:
```python
def is_even(n: int) -> bool:
    pass


if __name__ == "__main__":
    # Test your function
    is_even(4)    # True
    is_even(7)    # False
    is_even(0)    # True
    is_even(-2)   # True
    is_even(-5)   # False
```

## Logic
- A number is even if it's divisible by 2
- Use the modulo operator `%`
- If `n % 2 == 0`, the number is even

## Note
- 0 is considered even
- Negative numbers can also be even or odd

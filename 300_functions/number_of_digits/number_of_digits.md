# Number of Digits

Write a function that counts the number of digits in an integer.

## Task
- Create a function `number_of_digits(n)` that takes an integer
- Return the count of digits

## Template:
```python
def number_of_digits(n: int) -> int:
    pass


if __name__ == "__main__":
    # Test your function
    print(number_of_digits(123))       # 3
    print(number_of_digits(0))         # 1
    print(number_of_digits(-456))      # 3
    print(number_of_digits(1000000))   # 7
    print(number_of_digits(7))         # 1
```

## Logic
- Count digits by repeatedly dividing by 10
- Handle negative numbers (count digits, not the sign)
- Zero has 1 digit

## Note
- Don't convert to string
- Use a loop and integer division
- Handle negative numbers correctly

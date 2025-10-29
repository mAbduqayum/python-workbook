# Number of Digits

Write a function that counts the number of digits in an integer.

## Task
- Create a function `number_of_digits(n)` that takes an integer
- Return the count of digits

## Function Signature
```python
def number_of_digits(n: int) -> int:
    pass
```

## Examples
```python
number_of_digits(123)       # 3
number_of_digits(0)         # 1
number_of_digits(-456)      # 3
number_of_digits(1000000)   # 7
number_of_digits(7)         # 1
```

## Logic
- Count digits by repeatedly dividing by 10
- Handle negative numbers (count digits, not the sign)
- Zero has 1 digit

## Note
- Don't convert to string
- Use a loop and integer division
- Handle negative numbers correctly

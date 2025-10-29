# Digit Sum

Write a function that calculates the sum of digits in an integer.

## Task
- Create a function `digit_sum(n)` that takes an integer
- Return the sum of all digits

## Function Signature
```python
def digit_sum(n: int) -> int:
    pass
```

## Examples
```python
digit_sum(123)       # 6 (1 + 2 + 3)
digit_sum(0)         # 0
digit_sum(-456)      # 15 (4 + 5 + 6)
digit_sum(1000)      # 1 (1 + 0 + 0 + 0)
digit_sum(99)        # 18 (9 + 9)
```

## Logic
- Extract each digit using modulo 10
- Add the digit to sum
- Remove the digit using integer division by 10
- Repeat until no digits remain

## Note
- Don't convert to string
- Handle negative numbers (sum the digits, ignore the sign)
- Use a loop

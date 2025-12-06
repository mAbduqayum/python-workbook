# Digit Sum

Write a function that calculates the sum of digits in an integer.

## Task
- Create a function `digit_sum(n)` that takes an integer
- Return the sum of all digits

## Template:
```python
def digit_sum(n: int) -> int:
    pass


if __name__ == "__main__":
    # Test your function
    print(digit_sum(123))       # 6
    print(digit_sum(0))         # 0
    print(digit_sum(-456))      # 15
    print(digit_sum(1000))      # 1
    print(digit_sum(99))        # 18
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

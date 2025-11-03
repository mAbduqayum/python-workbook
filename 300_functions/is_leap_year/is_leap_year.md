# Is Leap Year

Write a function that determines if a year is a leap year.

## Task
- Create a function `is_leap_year(year)` that takes a year
- Return `True` if it's a leap year, `False` otherwise

## Template:
```python
def is_leap_year(year: int) -> bool:
    pass


if __name__ == "__main__":
    # Test your function
    is_leap_year(2000)    # True
    is_leap_year(2004)    # True
    is_leap_year(1900)    # False
    is_leap_year(2001)    # False
    is_leap_year(2024)    # True
```

## Logic
A year is a leap year if:
- It's divisible by 4, AND
- If it's divisible by 100, it must also be divisible by 400

## Note
- Year 2000 was a leap year (divisible by 400)
- Year 1900 was NOT a leap year (divisible by 100 but not by 400)
- Most years divisible by 4 are leap years

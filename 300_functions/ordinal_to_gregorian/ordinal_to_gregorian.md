# Ordinal to Gregorian Date

Write a function that converts an ordinal date (year + day of year) to Gregorian date (year, month, day).

## Task
- Create a function `ordinal_to_gregorian(year, day_of_year)` 
- Return a tuple (year, month, day)

## Template:
```python
def ordinal_to_gregorian(year: int, day_of_year: int) -> tuple[int, int, int]:
    pass


if __name__ == "__main__":
    # Test your function
    ordinal_to_gregorian(2024, 1)      # (2024, 1, 1)
    ordinal_to_gregorian(2024, 32)     # (2024, 2, 1)
    ordinal_to_gregorian(2024, 60)     # (2024, 2, 29)
    ordinal_to_gregorian(2023, 60)     # (2023, 3, 1)
    ordinal_to_gregorian(2024, 366)    # (2024, 12, 31)
```

## Logic
- Days per month: [31, 28/29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
- February has 29 days in leap years, 28 otherwise
- Subtract days from each month until remaining days fit in current month

## Note
- Account for leap years
- Return tuple of (year, month, day)
- Assume valid input (day_of_year is valid for the given year)

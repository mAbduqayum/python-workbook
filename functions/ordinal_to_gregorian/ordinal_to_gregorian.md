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
    print(ordinal_to_gregorian(2024, 1))      # (2024, 1, 1)
    print(ordinal_to_gregorian(2024, 32))     # (2024, 2, 1)
    print(ordinal_to_gregorian(2024, 60))     # (2024, 2, 29)
    print(ordinal_to_gregorian(2023, 60))     # (2023, 3, 1)
    print(ordinal_to_gregorian(2024, 366))    # (2024, 12, 31)
```

# Gregorian to Ordinal Date

Write a function that converts a Gregorian date to ordinal date (day of year).

## Task
- Create a function `gregorian_to_ordinal(year, month, day)` 
- Return the day of the year (1-366)

## Function Signature
```python
def gregorian_to_ordinal(year: int, month: int, day: int) -> int:
    pass
```

## Examples
```python
gregorian_to_ordinal(2024, 1, 1)      # 1
gregorian_to_ordinal(2024, 2, 1)      # 32
gregorian_to_ordinal(2024, 2, 29)     # 60 (leap year)
gregorian_to_ordinal(2023, 3, 1)      # 60 (not leap year)
gregorian_to_ordinal(2024, 12, 31)    # 366
```

## Logic
- Sum days from all previous months
- Add the current day
- Account for leap years when month > 2

## Note
- February has 29 days in leap years, 28 otherwise
- Days per month: [31, 28/29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
- Return integer day of year

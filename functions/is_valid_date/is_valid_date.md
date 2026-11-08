# Valid Date

Write functions that check whether a year, month and day make a real date.

## Task
- Create a function `days_in_month(year, month)` that returns how many days that month has, for a month from 1 to 12
- Create a function `is_valid_date(year, month, day)` that returns `True` if the date exists, `False` otherwise
- February has 29 days in a leap year; copy your `is_leap_year` from [Is Leap Year](../is_leap_year/is_leap_year.md)

## Examples

| Call                         | Returns |
|------------------------------|---------|
| `days_in_month(2023, 4)`     | `30`    |
| `days_in_month(2024, 2)`     | `29`    |
| `days_in_month(2023, 2)`     | `28`    |
| `is_valid_date(2024, 2, 29)` | `True`  |
| `is_valid_date(2023, 2, 29)` | `False` |
| `is_valid_date(2023, 4, 31)` | `False` |
| `is_valid_date(2023, 13, 1)` | `False` |
| `is_valid_date(2023, 12, 0)` | `False` |

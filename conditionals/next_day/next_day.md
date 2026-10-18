# Exercise: Next Day

Write a program that reads a date and computes its immediate successor (next day). Print the year, month, and day of the next day on one line, separated by spaces.

## Examples
**Example 1:** (Regular day)
```
2019
11
18
```
```
2019 11 19
```

**Example 2:** (End of month)
```
2019
11
30
```
```
2019 12 1
```

**Example 3:** (End of year)
```
2019
12
31
```
```
2020 1 1
```

**Example 4:** (Leap year)
```
2020
2
28
```
```
2020 2 29
```

**Example 5:** (Non-leap year)
```
2021
2
28
```
```
2021 3 1
```

## Days in Each Month
| Month                 | Days     | Notes                |
|-----------------------|----------|----------------------|
| 1, 3, 5, 7, 8, 10, 12 | 31       |                      |
| 4, 6, 9, 11           | 30       |                      |
| 2                     | 28 or 29 | Depends on leap year |

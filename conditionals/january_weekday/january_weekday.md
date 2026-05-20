# Exercise: What Day of the Week Is January 1?

Write a program that determines the day of the week for January 1st of a given year using a mathematical formula.

## Formula
```
day_of_week = (year + floor((year - 1) / 4) - floor((year - 1) / 100) + floor((year - 1) / 400)) % 7
```

## Day Mapping
| Result | Day of Week |
|--------|-------------|
| 0      | Sunday      |
| 1      | Monday      |
| 2      | Tuesday     |
| 3      | Wednesday   |
| 4      | Thursday    |
| 5      | Friday      |
| 6      | Saturday    |

## Examples
**Example 1:**
```
2020
```
```
Wednesday
```

**Example 2:**
```
2021
```
```
Friday
```

**Example 3:**
```
2022
```
```
Saturday
```

**Example 4:**
```
2000
```
```
Saturday
```

**Example 5:**
```
1900
```
```
Monday
```

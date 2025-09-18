# Exercise: Units of Time

Write a program that converts a duration given in days, hours, minutes, and seconds to total seconds.

## Task

- Read number of days (as `int`)
- Read number of hours (as `int`)
- Read number of minutes (as `int`)
- Read number of seconds (as `int`)
- Calculate and display total seconds

## Examples

**Example 1:**

```
Enter days: 2
Enter hours: 3
Enter minutes: 45
Enter seconds: 30
```

```
Total seconds: 186330
```

**Example 2:**

```
Enter days: 1
Enter hours: 0
Enter minutes: 30
Enter seconds: 0
```

```
Total seconds: 88200
```

**Example 3:**

```
Enter days: 0
Enter hours: 2
Enter minutes: 15
Enter seconds: 45
```

```
Total seconds: 8145
```

## Formula

`total_seconds = days×86400 + hours×3600 + minutes×60 + seconds`

## Note

- `1 day = 86400 seconds`
- `1 hour = 3600 seconds`
- `1 minute = 60 seconds`

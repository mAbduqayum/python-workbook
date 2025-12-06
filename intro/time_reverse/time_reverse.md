# Exercise: Units of Time (Again)

Write a program that converts total seconds into days, hours, minutes, and seconds format.

## Task

- Read total number of seconds (as `int`)
- Convert to days, hours, minutes, and remaining seconds
- Display in `D:HH:MM:SS` format

## Examples

**Example 1:**

```
Enter total seconds: 186330
```

```
Time format: 2:03:45:30
```

**Example 2:**

```
Enter total seconds: 88200
```

```
Time format: 1:00:30:00
```

**Example 3:**

```
Enter total seconds: 8145
```

```
Time format: 0:02:15:45
```

## Formula

- `days = seconds // 86400`
- `hours = (seconds % 86400) // 3600`
- `minutes = (seconds % 3600) // 60`
- `remaining_seconds = seconds % 60`

## Note

- Use integer division (`//`) and modulo (`%`)
- Format hours, minutes, and seconds with leading zeros: `:02d`

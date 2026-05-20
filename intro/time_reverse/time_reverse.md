# Exercise: Units of Time (Again)

Write a program that converts total seconds into days, hours, minutes, and seconds format.

## Examples

**Example 1:**

```
186330
```

```
Time format: 2:03:45:30
```

**Example 2:**

```
88200
```

```
Time format: 1:00:30:00
```

**Example 3:**

```
8145
```

```
Time format: 0:02:15:45
```

## Formula

- `days = seconds // 86400`
- `hours = (seconds % 86400) // 3600`
- `minutes = (seconds % 3600) // 60`
- `remaining_seconds = seconds % 60`

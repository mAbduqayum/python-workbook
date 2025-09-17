# Sorted Order

Write a program that determines if three numbers are sorted in ascending order, descending order, or random order.

## Task
- Read three numbers a, b, and c from the user
- Determine their order: ascending, descending, or random
- Display the appropriate classification

## Examples
**Example 1:**
```
1
5
9
ascending
```

**Example 2:**
```
9
5
1
descending
```

**Example 3:**
```
5
1
9
random
```

**Example 4:**
```
3
3
7
ascending
```

**Example 5:**
```
8
4
4
descending
```

**Example 6:**
```
2
2
2
ascending
```

## Logic
- **Ascending**: a ≤ b ≤ c
- **Descending**: a ≥ b ≥ c
- **Random**: neither ascending nor descending

## Note
- Allow equal adjacent values (non-strict ordering)
- If all three are equal, consider it ascending
- Handle ties appropriately (e.g., 3,3,7 is ascending)
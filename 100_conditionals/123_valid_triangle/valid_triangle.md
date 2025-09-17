# Valid Triangle

Write a program that determines if three side lengths can form a valid triangle.

## Task
- Read three side lengths from the user
- Determine if they can form a valid triangle
- Display "valid triangle" or "invalid triangle"

## Triangle Inequality Theorem
For sides a, b, and c to form a valid triangle:
- a + b > c
- a + c > b
- b + c > a

All three conditions must be true.

## Examples
**Example 1:**
```
3
4
5
```
```
valid triangle
```

**Example 2:**
```
1
2
5
```
```
invalid triangle
```

**Example 3:**
```
6
8
10
```
```
valid triangle
```

**Example 4:**
```
1
1
3
```
```
invalid triangle
```

**Example 5:**
```
5
5
5
```
```
valid triangle
```

## Note
- All sides must be positive
- Sum of any two sides must be greater than the third side
- Check all three combinations of the triangle inequality
- Use logical AND to combine all conditions
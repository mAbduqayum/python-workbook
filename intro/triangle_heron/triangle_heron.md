# Exercise: Area of a Triangle (Again)

Write a program that calculates the area of a triangle using Heron's formula when all three side lengths are known.

## Task

- Read the lengths of all three sides (as `float`)
- Calculate and display the area using Heron's formula
- Triangle sides are guaranteed to form a valid triangle

## Examples

**Example 1:**

```
Enter length of side 1: 3
Enter length of side 2: 4
Enter length of side 3: 5
```

```
Area of triangle: 6.00
```

**Example 2:**

```
Enter length of side 1: 5
Enter length of side 2: 6
Enter length of side 3: 7
```

```
Area of triangle: 14.70
```

**Example 3:**

```
Enter length of side 1: 10
Enter length of side 2: 10
Enter length of side 3: 12
```

```
Area of triangle: 48.00
```

## Formula

- `s = (s1 + s2 + s3) / 2` (semi-perimeter)
- `Area = √(s × (s - s1) × (s - s2) × (s - s3))`

## Note

- Use `.2f` formatting to display 2 decimal places
- Use `math.sqrt()` for square root calculation

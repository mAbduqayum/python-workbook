# Exercise: Area of a Triangle (Again)

Write a program that calculates the area of a triangle using Heron's formula when all three side lengths are known.

## Task

- Read the lengths of all three sides (as `float`)
- Calculate and display the area using Heron's formula
- Triangle sides are guaranteed to form a valid triangle

## Examples

**Example 1:**

```
3
4
5
```

```
Area of triangle: 6.00
```

**Example 2:**

```
5
6
7
```

```
Area of triangle: 14.70
```

**Example 3:**

```
10
10
12
```

```
Area of triangle: 48.00
```

## Formula

- `s = (s1 + s2 + s3) / 2` (semi-perimeter)
- `Area = √(s × (s - s1) × (s - s2) × (s - s3))`

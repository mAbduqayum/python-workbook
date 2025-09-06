# Exercise: Area of a Regular Polygon

Write a program that calculates the area of a regular polygon given the number of sides and side length.

## Task
- Read the number of sides (as `int`)
- Read the length of each side (as `float`)
- Calculate and display the area

## Examples
**Example 1:**
```
Enter number of sides: 6
Enter side length: 4
Area of regular polygon: 41.57
```

**Example 2:**
```
Enter number of sides: 8
Enter side length: 3
Area of regular polygon: 43.46
```

**Example 3:**
```
Enter number of sides: 5
Enter side length: 5
Area of regular polygon: 43.01
```

## Formula
`Area = (n × s²) / (4 × tan(π/n))` where:
- `n` = number of sides
- `s` = side length

## Note
- Use `.2f` formatting to display 2 decimal places
- Use `math.tan()` and `math.pi`
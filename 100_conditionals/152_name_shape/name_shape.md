# Exercise 104: Name That Shape

Write a program that determines the name of a shape from its number of sides. The program should support shapes with 3 to 10 sides and display an appropriate error message for numbers outside this range.

## Task
- Read the number of sides from the user
- Report the appropriate shape name as part of a meaningful message
- Support shapes with 3 to 10 sides
- Display an error message for numbers outside the valid range

## Shape Names
| Sides | Shape Name    |
|-------|---------------|
| 3     | Triangle      |
| 4     | Quadrilateral |
| 5     | Pentagon      |
| 6     | Hexagon       |
| 7     | Heptagon      |
| 8     | Octagon       |
| 9     | Nonagon       |
| 10    | Decagon       |

## Examples
**Example 1:**
```
3
Triangle
```

**Example 2:**
```
6
Hexagon
```

**Example 3:**
```
10
Decagon
```

**Example 4:**
```
2
Invalid number of sides
```

**Example 5:**
```
15
Invalid number of sides
```

## Note
- Handle edge cases for numbers less than 3 and greater than 10
- Use appropriate conditional statements (if-elif-else) to check for each shape
- Provide meaningful error messages for invalid input

# Exercise 107: Classifying Triangles

A triangle can be classified based on the lengths of its sides as equilateral, isosceles, or scalene. Write a program that reads the lengths of three sides and determines the triangle's type.

## Task
- Read the lengths of the three sides of a triangle from the user
- Determine and display the triangle's classification
- Handle the three types of triangles appropriately

## Triangle Classifications
- **Equilateral**: All three sides have the same length
- **Isosceles**: Two sides have the same length, and the third side has a different length
- **Scalene**: All three sides have different lengths

## Examples
**Example 1:**
```
3
3
3
equilateral
```

**Example 2:**
```
5
5
8
isosceles
```

**Example 3:**
```
3
4
5
scalene
```

**Example 4:**
```
7
9
7
isosceles
```

## Note
- Consider all possible arrangements for isosceles triangles (sides 1&2, 1&3, or 2&3 could be equal)
- Check for equilateral first (all sides equal), then isosceles (any two sides equal), then scalene (all different)
- This exercise focuses on classification only, not triangle validity
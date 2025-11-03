# Is Valid Triangle

Write a function that determines if three sides can form a valid triangle.

## Task
- Create a function `is_valid_triangle(a, b, c)` that takes three side lengths
- Return `True` if they can form a valid triangle, `False` otherwise

## Template:
```python
def is_valid_triangle(a: float, b: float, c: float) -> bool:
    pass


if __name__ == "__main__":
    # Test your function
    is_valid_triangle(3, 4, 5)      # True
    is_valid_triangle(1, 2, 3)      # False
    is_valid_triangle(5, 5, 5)      # True
    is_valid_triangle(1, 1, 10)     # False
    is_valid_triangle(7, 10, 5)     # True
```

## Logic
Triangle Inequality Theorem: The sum of any two sides must be greater than the third side.
- a + b > c
- a + c > b
- b + c > a

All three conditions must be true.

## Note
- All sides must be positive numbers
- If any side is 0 or negative, it's not a valid triangle
- Equal sides are allowed (equilateral or isosceles triangles)

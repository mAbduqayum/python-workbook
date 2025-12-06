# Quadratic Roots

Write a function that calculates the roots of a quadratic equation.

## Task
- Create a function `quadratic_roots(a, b, c)` for equation ax² + bx + c = 0
- Return a tuple of roots (root1, root2)
- If there are no real roots, return None

## Template:
```python
def quadratic_roots(a: float, b: float, c: float) -> tuple[float, float] | None:
    pass


if __name__ == "__main__":
    # Test your function
    print(quadratic_roots(1, -3, 2))     # (2.0, 1.0)
    print(quadratic_roots(1, 0, -4))     # (2.0, -2.0)
    print(quadratic_roots(1, -2, 1))     # (1.0, 1.0)
    print(quadratic_roots(1, 0, 1))      # None
```

## Formula
- Discriminant: Δ = b² - 4ac
- If Δ < 0: no real roots
- Root 1: (-b + √Δ) / (2a)
- Root 2: (-b - √Δ) / (2a)

## Note
- Use `math.sqrt()` for square root
- Return the larger root first
- Handle the case when discriminant is negative

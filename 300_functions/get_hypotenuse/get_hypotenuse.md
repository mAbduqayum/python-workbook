# Get Hypotenuse

Write a function that calculates the hypotenuse of a right triangle.

## Task
- Create a function `get_hypotenuse(a, b)` that takes two sides of a right triangle
- Return the length of the hypotenuse

## Template:
```python
def get_hypotenuse(a: float, b: float) -> float:
    pass


if __name__ == "__main__":
    # Test your function
    get_hypotenuse(3, 4)      # 5.0
    get_hypotenuse(5, 12)     # 13.0
    get_hypotenuse(8, 15)     # 17.0
    get_hypotenuse(1, 1)      # 1.4142135623730951
```

## Formula
- Hypotenuse = √(a² + b²) (Pythagorean theorem)
- Use `math.sqrt()` for the square root

## Note
- Import the `math` module
- Both sides should be positive numbers
- Result should be a float

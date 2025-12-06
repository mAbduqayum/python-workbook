# Normalize Fraction

Write a function that normalizes (simplifies) a fraction to its lowest terms.

## Task
- Create a function `normalize_fraction(numerator, denominator)` 
- Return a tuple (simplified_numerator, simplified_denominator)

## Template:
```python
def normalize_fraction(numerator: int, denominator: int) -> tuple[int, int]:
    pass


if __name__ == "__main__":
    # Test your function
    print(normalize_fraction(4, 8))       # (1, 2)
    print(normalize_fraction(6, 9))       # (2, 3)
    print(normalize_fraction(5, 10))      # (1, 2)
    print(normalize_fraction(7, 3))       # (7, 3)
    print(normalize_fraction(0, 5))       # (0, 1)
```

## Logic
- Find the Greatest Common Divisor (GCD) of numerator and denominator
- Divide both by the GCD
- Special case: if numerator is 0, return (0, 1)

## Note
- Use the Euclidean algorithm to find GCD
- Both numerator and denominator should be positive in result
- Handle the case where numerator is 0

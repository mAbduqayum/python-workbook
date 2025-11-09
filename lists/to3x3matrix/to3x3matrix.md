# To 3x3 Matrix

Create a function to convert a string of 9 integers into a 3x3 matrix.

## Template:

```python
def to3x3matrix(string: str) -> list[list[int]]:
    pass


if __name__ == "__main__":
    # Test your function
    matrix = to3x3matrix("1 2 3 4 5 6 7 8 9")
    for row in matrix:
        print(row)
    # Output:
    # [1, 2, 3]
    # [4, 5, 6]
    # [7, 8, 9]
```

## Note

- The string contains exactly 9 space-separated integers
- The matrix is always 3x3
- Each row is a sublist of 3 elements

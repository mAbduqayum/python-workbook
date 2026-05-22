# To Matrix

Convert a flat list into a matrix with specified dimensions (general form).

## Task

- Create a function `to_matrix(numbers, rows, cols)` that takes a list and dimensions
- Return a 2D list (matrix) with the specified number of rows and columns

## Template:

```python
def to_matrix(numbers: list[int], rows: int, cols: int) -> list[list[int]]:
    pass


if __name__ == "__main__":
    # Test your function
    print(to_matrix([1, 2, 3, 4, 5, 6], 2, 3))
    # [[1, 2, 3], [4, 5, 6]]
    
    print(to_matrix([1, 2, 3, 4], 2, 2))
    # [[1, 2], [3, 4]]
```

## Note

- Assume `len(numbers) == rows * cols`

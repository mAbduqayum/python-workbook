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

<details>
<summary><strong>Hint</strong></summary>

- Use list comprehension with slicing
- For each row i, extract elements from index i*cols to (i+1)*cols
- `[numbers[i*cols:(i+1)*cols] for i in range(rows)]`

</details>

## Note

- Assume len(numbers) == rows * cols
- Each row contains exactly cols elements
- This is a generalization of the 3x3 matrix function

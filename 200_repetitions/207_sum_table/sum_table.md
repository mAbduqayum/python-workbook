# Sum Table

Create a table showing the sum of row and column numbers.

## Task
- Read a positive integer `n` from the user
- Display an `n x n` table where each cell contains the sum of its row and column indices
- Row and column indices start from 1
- Format the table with proper spacing

## Examples
**Example 1:**
```
5
```
```
 2  3  4  5  6
 3  4  5  6  7
 4  5  6  7  8
 5  6  7  8  9
 6  7  8  9 10
```

**Example 2:**
```
3
```
```
 2  3  4
 3  4  5
 4  5  6
```

## Logic
- Use nested loops: outer for rows (1 to n), inner for columns (1 to n)
- For each position (row, col), calculate: row + col
- Use formatting to align numbers: `print(value, end="  ")` or `f"{value:2}"` for spacing
- Print a newline after each row

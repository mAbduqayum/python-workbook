# Sum Table

Create a table showing the sum of row and column numbers.

## Task
- Read a positive integer `n` from the user
- Display an `(n+1) x (n+1)` table where each cell contains the sum of its row and column indices
- Row and column indices range from 0 to n (inclusive)
- Format the table with proper spacing

## Examples
**Example 1:**
```
5
```
```
 0  1  2  3  4  5
 1  2  3  4  5  6
 2  3  4  5  6  7
 3  4  5  6  7  8
 4  5  6  7  8  9
 5  6  7  8  9 10
```

**Example 2:**
```
3
```
```
 0  1  2  3
 1  2  3  4
 2  3  4  5
 3  4  5  6
```

## Logic
- Use nested loops: outer for rows (0 to n), inner for columns (0 to n)
- For each position (row, col), calculate: row + col
- Use formatting to align numbers: `print(value, end="  ")` or `f"{value:2}"` for spacing
- Print a newline after each row

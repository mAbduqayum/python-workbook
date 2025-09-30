# Multiplication Table

Display a multiplication table showing products from 1×1 to 10×10.

## Task
- Create a multiplication table for 1 through 10
- Include row labels (1-10) on the left
- Include column labels (1-10) on the top
- Display all products in a formatted grid

## Expected Output
```
    1   2   3   4   5   6   7   8   9  10
1   1   2   3   4   5   6   7   8   9  10
2   2   4   6   8  10  12  14  16  18  20
3   3   6   9  12  15  18  21  24  27  30
4   4   8  12  16  20  24  28  32  36  40
5   5  10  15  20  25  30  35  40  45  50
6   6  12  18  24  30  36  42  48  54  60
7   7  14  21  28  35  42  49  56  63  70
8   8  16  24  32  40  48  56  64  72  80
9   9  18  27  36  45  54  63  72  81  90
10 10  20  30  40  50  60  70  80  90 100
```

## Logic
- Use nested for loops:
  - Outer loop for rows (1-10)
  - Inner loop for columns (1-10)
- First, print the header row with column numbers
- Then for each row:
  - Print the row number
  - Print each product (row × column)
  - Use end="" to stay on same line

## Hints
- print(value, end="") prevents moving to next line
- print(value, end=" ") adds space between values
- Use nested loops: outer for rows, inner for columns
- Format numbers with proper spacing for alignment

# Repetition in Python - Nested Loops

A loop inside another loop is called a **nested loop**. The inner loop runs
completely for each iteration of the outer loop.

## How They Run

Watch the two variables. `col` goes all the way through for each value of `row`:

```python
for row in range(2):
    for col in range(3):
        print(row, col)
```

**Output:**

```
0 0
0 1
0 2
1 0
1 1
1 2
```

The `print` runs 2 × 3 = 6 times: the outer loop's iterations times the inner
loop's.

## Rows and Columns

Most nested loops work on a grid. The outer loop goes through the rows, and the
inner loop through the columns of one row. `end=" "` keeps a row on one line, and
the empty `print()` after the inner loop ends that line:

```python
for row in range(3):
    for col in range(4):
        print("*", end=" ")
    print()
```

**Output:**

```
* * * *
* * * *
* * * *
```

## When the Inner Loop Depends on the Outer

The inner loop's range can use the outer variable, so that each row has a
different length:

```python
n = int(input())

for row in range(1, n + 1):
    for col in range(1, row + 1):
        print(col, end=" ")
    print()
```

**Output (for n = 4):**

```
1
1 2
1 2 3
1 2 3 4
```

## Resetting a Variable for Each Row

A variable that belongs to one row is set up inside the outer loop, so that it
starts again for every row:

```python
for row in range(1, 4):
    row_total = 0
    for col in range(1, 4):
        row_total += row * col
    print(f"Row {row}: {row_total}")
```

**Output:**

```
Row 1: 6
Row 2: 12
Row 3: 18
```

Move `row_total = 0` above the outer loop and the total never resets, so it
prints 6, 18 and 36. When a nested loop gives a wrong answer, check first where
its variables start.

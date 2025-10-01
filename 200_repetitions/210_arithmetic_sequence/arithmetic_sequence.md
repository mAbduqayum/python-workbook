# Arithmetic Sequence

Generate and display an arithmetic sequence.

## Task
- Read three integers from the user:
  - `start`: first term of the sequence
  - `end`: upper limit (inclusive)
  - `diff`: common difference between consecutive terms
- Display all terms of the arithmetic sequence from start to end
- Each term on its own line
- If `diff` is 0 or has wrong sign, display an error message

## Examples
**Example 1:**
```
5
20
3
```
```
5
8
11
14
17
20
```

**Example 2:**
```
10
1
-2
```
```
10
8
6
4
2
```

**Example 3:**
```
1
10
0
```
```
Error: diff must be non-zero
```

## Logic
- Start with the first term
- Use a while loop to generate terms
- Add `diff` to get the next term
- Continue while the term is within bounds (≤ end if diff > 0, ≥ end if diff < 0)

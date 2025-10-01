# Arithmetic Sequence

Generate and display an arithmetic sequence.

## Task
- Read three integers from the user:
  - `start`: first term of the sequence
  - `end`: upper limit (inclusive)
  - `diff`: common difference between consecutive terms
- Display all terms of the arithmetic sequence from start to end
- Each term on its own line
- **Note:** You can assume that the inputs are always valid (diff is non-zero and has the correct sign)

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

**Note:** Since inputs are guaranteed to be valid, there are no error cases to consider.

## Logic
- Start with the first term
- Use a while loop to generate terms
- Add `diff` to get the next term
- Continue while the term is within bounds (≤ end if diff > 0, ≥ end if diff < 0)

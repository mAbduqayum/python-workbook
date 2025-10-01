# Geometric Sequence

Generate and display a geometric sequence.

## Task
- Read three values from the user:
  - `start`: first term of the sequence (float)
  - `count`: number of terms to generate (integer)
  - `ratio`: common ratio between consecutive terms (float)
- Display the first `count` terms of the geometric sequence
- Each term on its own line
- If `count` is less than 1, display an error message

## Examples
**Example 1:**
```
2
5
3
```
```
2.0
6.0
18.0
54.0
162.0
```

**Example 2:**
```
100
4
0.5
```
```
100.0
50.0
25.0
12.5
```

**Example 3:**
```
5
0
2
```
```
Error: count must be at least 1
```

## Logic
- Start with the first term
- Use a for loop to generate `count` terms
- Multiply by `ratio` to get the next term
- Display each term

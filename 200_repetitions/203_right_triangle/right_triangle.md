# Right Triangle Art

Create a right triangle pattern using asterisks.

## Task
- Read a positive integer `n` from the user
- Display a right triangle with `n` rows
- Each row `i` should contain `i` asterisks
- If `n` is less than 1, display an error message

## Examples
**Example 1:**
```
5
```
```
*
**
***
****
*****
```

**Example 2:**
```
3
```
```
*
**
***
```

**Example 3:**
```
0
```
```
Error: n must be at least 1
```

## Logic
- Use a for loop to iterate from 1 to n (inclusive)
- For each row i, print i asterisks
- Use string multiplication: `"*" * i`

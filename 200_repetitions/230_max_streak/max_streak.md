# Maximum Streak

Find the longest consecutive streak of identical values.

## Task
- Read integers from the user until a blank line is entered
- Find the maximum streak (consecutive identical values)
- Display the streak length and the value that formed the streak
- Display an error message if no values were entered

## Examples
**Example 1:**
```
1
1
1
2
2
3
3
3
3

```
```
Maximum streak: 4 of value 3
```

**Example 2:**
```
5
5
5
5
5

```
```
Maximum streak: 5 of value 5
```

**Example 3:**
```
1
2
3
4

```
```
Maximum streak: 1 of value 1
```

**Example 4:**
```

```
```
Error: No values provided
```

## Logic
- Track current streak length and value
- Track maximum streak length and value
- As you read each value:
  - If same as previous: increment current streak
  - If different: compare current streak to max, then reset current streak
- After loop ends, compare final streak to max

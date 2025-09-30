# Compute a Grade Point Average

Calculate the GPA of an arbitrary number of letter grades.

## Task
- Read letter grades from the user until a blank line is entered
- Convert each letter grade to grade points
- Calculate and display the grade point average

## Examples
**Example 1:**
```
A
C+
B

```
```
3.1
```

**Example 2:**
```
A+
A
A-

```
```
4.0
```

## Grade Points Table
| Letter | Points | Letter | Points |
|--------|--------|--------|--------|
| A+     | 4.0    | C+     | 2.3    |
| A      | 4.0    | C      | 2.0    |
| A-     | 3.7    | C-     | 1.7    |
| B+     | 3.3    | D+     | 1.3    |
| B      | 3.0    | D      | 1.0    |
| B-     | 2.7    | F      | 0.0    |

## Logic
- Use a while loop to read grades until blank line
- Convert each grade to points using if/elif statements or dictionary
- Keep running sum of grade points
- Count number of grades
- GPA = total grade points / number of grades

## Hints
- Read input as string to detect blank line
- Strip whitespace from input
- Use a dictionary for grade-to-point mapping
- No error checking needed (assume valid input)

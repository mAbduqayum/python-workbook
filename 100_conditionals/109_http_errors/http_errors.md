# Exercise: HTTP Status Code Categories

Write a program that reads an HTTP status code from the user and displays the corresponding category.

## Task
- Read an HTTP status code from the user (as `int`)
- Display the category based on the first digit
- Display `Unknown status code` if it doesn't fit these categories

## HTTP Status Code Categories
| Range   | Category      |
|---------|---------------|
| 100-199 | Informational |
| 200-299 | Success       |
| 300-399 | Redirection   |
| 400-499 | Client Error  |
| 500-599 | Server Error  |

## Examples
**Example 1:**
```
200
```
```
Success
```

**Example 2:**
```
404
```
```
Client Error
```

**Example 3:**
```
999
```
```
Unknown status code
```

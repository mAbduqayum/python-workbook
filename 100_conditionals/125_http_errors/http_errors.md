# Exercise 125: HTTP Status Codes

Write a program that reads an HTTP status code from the user and displays the corresponding error message and description.

## Task
- Read an HTTP status code from the user
- Display the status code name and description
- Display an appropriate error message if the status code is not recognized

## HTTP Status Code Reference Table
| Code | Name                  | Description                           |
|------|-----------------------|---------------------------------------|
| 200  | OK                    | The request was successful            |
| 301  | Moved Permanently     | The resource has moved permanently    |
| 400  | Bad Request           | The request could not be understood   |
| 401  | Unauthorized          | Authentication is required            |
| 403  | Forbidden             | Access to the resource is denied      |
| 404  | Not Found             | The requested resource was not found  |
| 500  | Internal Server Error | The server encountered an error       |
| 502  | Bad Gateway           | Invalid response from upstream server |
| 503  | Service Unavailable   | The server is temporarily unavailable |

## Examples
**Example 1:**
```
200
```
```
200 OK: The request was successful
```

**Example 2:**
```
404
```
```
404 Not Found: The requested resource was not found
```

**Example 3:**
```
500
```
```
500 Internal Server Error: The server encountered an error
```

**Example 4:**
```
401
```
```
401 Unauthorized: Authentication is required
```

**Example 5:**
```
999
```
```
Unknown status code
```
# Password Strength

Evaluate password strength based on character types, length, and special characters.

## Task
- Read a password from the user
- Check for five criteria:
  - Contains at least one uppercase letter
  - Contains at least one lowercase letter
  - Contains at least one digit
  - Contains at least one special character `!@#$%^&*()_+-=[]{}|;:,.<>?`
  - Password length is at least 8 characters
- Display the strength level based on criteria met:
  - **very weak**: 1 criteria met
  - **weak**: 2 criteria met
  - **medium**: 3 criteria met
  - **strong**: 4 criteria met
  - **very strong**: 5 criteria met (all criteria)

## Examples
**Example 1:**
```
Hello123!@#
```
```
very strong
```

**Example 2:**
```
hello123
```
```
medium
```

# Password Strength

Evaluate password strength based on character types.

## Task
- Read a password from the user
- Check for three criteria:
  - Contains at least one uppercase letter
  - Contains at least one lowercase letter
  - Contains at least one digit
- Display the strength level:
  - **Weak**: 0-1 criteria met
  - **Moderate**: 2 criteria met
  - **Strong**: 3 criteria met

## Examples
**Example 1:**
```
Hello123
```
```
Strong
```

**Example 2:**
```
hello123
```
```
Moderate
```

**Example 3:**
```
hello
```
```
Weak
```

**Example 4:**
```
12345
```
```
Weak
```

## Logic
- Initialize three boolean flags: has_upper, has_lower, has_digit
- Loop through each character in the password:
  - Check if uppercase: set has_upper to True
  - Check if lowercase: set has_lower to True
  - Check if digit: set has_digit to True
- Count how many criteria are met
- Display strength based on count

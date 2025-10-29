# Random Password Generator

Write a function that generates a random password.

## Task
- Create a function `password(length)` that generates a random password
- Include lowercase letters, uppercase letters, digits, and special characters
- Return the generated password string

## Function Signature
```python
def password(length: int) -> str:
    pass
```

## Examples
```python
password(8)      # e.g., "aB3$xY9z"
password(12)     # e.g., "P@ssw0rd!123"
password(16)     # e.g., "aB3$xY9z!pQ7&mN2"
```

## Logic
- Define character sets: lowercase, uppercase, digits, special chars
- Randomly select characters from combined set
- Ensure password includes at least one from each category

## Note
- Use `random.choice()` to select random characters
- Character set: `abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()`
- Password should be secure and unpredictable
- For this exercise, simple random selection is acceptable

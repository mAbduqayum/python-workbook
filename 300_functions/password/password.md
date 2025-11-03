# Random Password Generator

Write a function that generates a random password.

## Task
- Create a function `password(length)` that generates a random password
- Include lowercase letters, uppercase letters, digits, and special characters
- Return the generated password string

## Template:
```python
def password(length: int) -> str:
    pass


if __name__ == "__main__":
    # Test your function
    password(8)      # Random 8-character password
    password(12)     # Random 12-character password
    password(16)     # Random 16-character password
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

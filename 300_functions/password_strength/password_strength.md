# Password Strength Checker

Write a function that evaluates password strength.

## Task
- Create a function `password_strength(pwd)` that evaluates a password
- Return a strength rating: "weak", "medium", or "strong"

## Template:
```python
def password_strength(pwd: str) -> str:
    pass


if __name__ == "__main__":
    # Test your function
    print(password_strength("abc"))           # "weak"
    print(password_strength("Password1"))     # "medium"
    print(password_strength("P@ssw0rd!"))     # "strong"
    print(password_strength("hello"))         # "weak"
    print(password_strength("Hello123"))      # "medium"
```

## Criteria
**Weak**: 
- Length < 8, OR
- Missing multiple character types

**Medium**:
- Length >= 8, AND
- Has at least 2 character types (lower, upper, digit, special)

**Strong**:
- Length >= 12, AND
- Has at least 3 character types

## Note
- Character types: lowercase, uppercase, digits, special characters
- Special characters: `!@#$%^&*()_+-=[]{}|;:,.<>?`
- Evaluate based on length and variety

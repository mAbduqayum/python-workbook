# Password Strength Checker

Write a function that evaluates password strength.

## Task
- Create a function `password_strength(pwd)` that evaluates a password
- Return a strength rating: "weak", "medium", or "strong"
- Special characters: `!@#$%^&*()_+-=[]{}|;:,.<>?`

## Examples

| Call                                | Returns    |
|-------------------------------------|------------|
| `password_strength("abc")`          | `"weak"`   |
| `password_strength("abcdefgh")`     | `"weak"`   |
| `password_strength("P@ssw0rd!")`    | `"medium"` |
| `password_strength("MyP@ssw0rd!2")` | `"strong"` |

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


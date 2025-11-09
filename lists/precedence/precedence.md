# Precedence

Return the precedence level of an operator.

## Task

- Create a function `precedence(op)` that takes an operator character
- Return an integer representing the precedence level
- Higher number means higher precedence

## Template:

```python
def precedence(operation: str) -> int:
    pass


if __name__ == "__main__":
    # Test your function
    print(precedence('+'))  # 1
    print(precedence('-'))  # 1
    print(precedence('*'))  # 2
    print(precedence('/'))  # 2
    print(precedence('^'))  # 3
    print(precedence('~'))  # 4 (unary minus)
```

## Note

- Higher precedence operations are performed first
- Unary operators typically have highest precedence
- Exponentiation has higher precedence than multiplication
- Used in converting infix to postfix notation

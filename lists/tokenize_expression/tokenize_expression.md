# Tokenize Expression

Parse a mathematical expression string into a list of tokens.

## Task

- Create a function `tokenize_expression(expr)` that takes an expression string
- Return a list of tokens (numbers, operators, parentheses)
- Handle multi-digit numbers

## Template:

```python
def tokenize_expression(expr: str) -> list[str]:
    pass


if __name__ == "__main__":
    # Test your function
    print(tokenize_expression("3+5*2"))  # ['3', '+', '5', '*', '2']
    print(tokenize_expression("(10+20)*3"))  # ['(', '10', '+', '20', ')', '*', '3']
    print(tokenize_expression("15 - 7 + 2"))  # ['15', '-', '7', '+', '2']
```

## Note

- Multi-digit numbers should be treated as single tokens
- Spaces should be ignored
- Support basic operators: +, -, *, /, ^
- Support parentheses: ( and )

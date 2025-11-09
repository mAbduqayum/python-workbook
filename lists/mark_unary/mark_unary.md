# Mark Unary

Mark unary operators (negative signs) in a tokenized expression.

## Task

- Create a function `mark_unary(tokens)` that takes a list of tokens
- Return a new list with unary minus operators marked (e.g., as '~')
- Distinguish between binary minus (subtraction) and unary minus (negation)

## Template:

```python
def mark_unary(tokens: list[str]) -> list[str]:
    pass


if __name__ == "__main__":
    # Test your function
    print(mark_unary(['-', '5', '+', '3']))  # ['~', '5', '+', '3']
    print(mark_unary(['(', '-', '5', ')', '*', '2']))  # ['(', '~', '5', ')', '*', '2']
    print(mark_unary(['3', '-', '5']))  # ['3', '-', '5']
```

<details>
<summary><strong>Hint</strong></summary>

- A minus is unary if:
    - It's at the beginning of the expression
    - It follows an opening parenthesis '('
    - It follows another operator
- Otherwise, it's binary (subtraction)
- Replace unary minus with a different symbol (e.g., '~')

</details>

## Note

- Unary minus: `-5` (negation)
- Binary minus: `3 - 5` (subtraction)
- This helps in expression evaluation

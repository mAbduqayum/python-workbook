# Infix to Postfix

Convert an infix expression to postfix notation (Reverse Polish Notation).

## Task

- Create a function `infix_to_postfix(tokens)` that takes a list of tokens in infix notation
- Return a list of tokens in postfix notation
- Use the Shunting Yard algorithm

## Template:

```python
def infix_to_postfix(tokens: list[str]) -> list[str]:
    pass


if __name__ == "__main__":
    # Test your function
    print(infix_to_postfix(['3', '+', '5', '*', '2']))
    # ['3', '5', '2', '*', '+']

    print(infix_to_postfix(['(', '3', '+', '5', ')', '*', '2']))
    # ['3', '5', '+', '2', '*']
```

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

<details>
<summary><strong>Hint (Shunting Yard Algorithm)</strong></summary>

- Create an output list and an operator stack
- For each token:
    - If number: add to output
    - If '(': push to stack
    - If ')': pop from stack to output until '('
    - If operator:
        - While stack top has higher/equal precedence: pop to output
        - Push current operator to stack
- After all tokens: pop remaining operators to output

</details>

## Note

- Postfix notation doesn't need parentheses
- Operators appear after their operands
- Example: `3 + 5` becomes `3 5 +`
- Easier to evaluate with a stack

<details>
<summary><strong>Historical Note</strong></summary>

Polish logician Jan Łukasiewicz invented prefix notation in 1924, seeking a parenthesis-free way to write logical formulas. Reverse Polish Notation (RPN)—postfix notation—reverses this idea, placing operators after operands. RPN gained widespread fame in the 1970s when Hewlett-Packard adopted it for their calculators, particularly the revolutionary HP-35. The Shunting Yard algorithm for converting infix to postfix was developed by computer science pioneer Edsger Dijkstra in the early 1960s, named for its resemblance to how trains are sorted in a railroad shunting yard.

</details>

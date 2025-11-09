# Evaluate Postfix

Evaluate a postfix expression and return the result.

## Task

- Create a function `evaluate_postfix(tokens)` that takes a list of tokens in postfix notation
- Return the numeric result of evaluating the expression

## Template:

```python
def evaluate_postfix(tokens: list[str]) -> float:
    pass


if __name__ == "__main__":
    # Test your function
    print(evaluate_postfix(['3', '5', '2', '*', '+']))  # 13.0 (3 + 5*2)
    print(evaluate_postfix(['3', '5', '+', '2', '*']))  # 16.0 ((3+5)*2)
    print(evaluate_postfix(['15', '7', '1', '1', '+', '-', '/']))  # 3.0
```

<details>
<summary><strong>Hint</strong></summary>

- Create an empty stack
- For each token:
    - If number: push to stack
    - If operator:
        - Pop two operands from stack (right, then left)
        - Apply operation: left op right
        - Push result back to stack
    - Special case for unary minus (~): pop one operand, negate it
- Final result is the only item left on stack

</details>

## Note

- Postfix expressions are evaluated left to right
- No need to worry about operator precedence
- Stack-based evaluation is straightforward
- Handle division by converting operands to float

<details>
<summary><strong>Historical Note</strong></summary>

Reverse Polish Notation (RPN) achieved widespread fame through HP calculators in the 1970s, particularly the HP-35 (1972), the world's first handheld scientific calculator. Engineers and scientists embraced RPN because it eliminated parentheses and enabled more efficient calculation workflows. Beyond calculators, stack-based evaluation of postfix expressions became fundamental to computer science—many programming language interpreters and virtual machines (including the Java Virtual Machine and Python's bytecode) execute code internally using stack-based postfix-like operations.

</details>

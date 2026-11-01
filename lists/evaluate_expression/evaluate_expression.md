# Evaluate Expression

Evaluate a mathematical expression from start to finish.

## Task

- Create a function `evaluate_expression(expr)` that takes an expression string
- Return its value as a float
- Operators: `+`, `-`, `*`, `/`, `^` and unary minus; parentheses: `(`, `)`

Solve the [`tokenize_expression`](../tokenize_expression/tokenize_expression.md),
[`mark_unary`](../mark_unary/mark_unary.md),
[`infix_to_postfix`](../infix_to_postfix/infix_to_postfix.md) and
[`evaluate_postfix`](../evaluate_postfix/evaluate_postfix.md) exercises first.
This function only has to call them in order, each one working on what the last
one returned.

## The Whole Process

Here is the process working on `-5 + 3 * 2`, where `~` marks the unary minus:

| Step                                 | Input              | Output             |
|--------------------------------------|--------------------|--------------------|
| Tokenize                             | `-5 + 3 * 2`       | `-, 5, +, 3, *, 2` |
| Mark unary minus                     | `-, 5, +, 3, *, 2` | `~, 5, +, 3, *, 2` |
| Convert to postfix, using precedence | `~, 5, +, 3, *, 2` | `5, ~, 3, 2, *, +` |
| Evaluate postfix                     | `5, ~, 3, 2, *, +` | `1.0`              |

## Template:

```python
from lists.evaluate_postfix.evaluate_postfix import evaluate_postfix
from lists.infix_to_postfix.infix_to_postfix import infix_to_postfix
from lists.mark_unary.mark_unary import mark_unary
from lists.tokenize_expression.tokenize_expression import tokenize_expression


def evaluate_expression(expr: str) -> float:
    pass


if __name__ == "__main__":
    # Test your function
    print(evaluate_expression("-5 + 3 * 2"))  # 1.0
    print(evaluate_expression("(10 + 20) * 3"))  # 90.0
```

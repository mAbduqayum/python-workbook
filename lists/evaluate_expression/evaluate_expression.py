from lists.evaluate_postfix.evaluate_postfix import evaluate_postfix
from lists.infix_to_postfix.infix_to_postfix import infix_to_postfix
from lists.mark_unary.mark_unary import mark_unary
from lists.tokenize_expression.tokenize_expression import tokenize_expression


def evaluate_expression(expr: str) -> float:
    tokens = tokenize_expression(expr)
    marked = mark_unary(tokens)
    postfix = infix_to_postfix(marked)
    return evaluate_postfix(postfix)


if __name__ == "__main__":
    print(evaluate_expression("-5 + 3 * 2"))  # 1.0
    print(evaluate_expression("(10 + 20) * 3"))  # 90.0

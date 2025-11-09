def evaluate_postfix(tokens: list[str]) -> float:
    stack = []
    operators = {'+', '-', '*', '/', '^'}

    for token in tokens:
        if token == '~':
            # Unary minus
            operand = stack.pop()
            stack.append(-operand)
        elif token in operators:
            # Binary operator
            right = stack.pop()
            left = stack.pop()

            if token == '+':
                result = left + right
            elif token == '-':
                result = left - right
            elif token == '*':
                result = left * right
            elif token == '/':
                result = left / right
            elif token == '^':
                result = left ** right

            stack.append(result)
        else:
            # Operand (number)
            stack.append(float(token))

    return stack[0]


if __name__ == "__main__":
    # Test your function
    print(evaluate_postfix(['3', '5', '2', '*', '+']))  # 13.0 (3 + 5*2)
    print(evaluate_postfix(['3', '5', '+', '2', '*']))  # 16.0 ((3+5)*2)
    print(evaluate_postfix(['15', '7', '1', '1', '+', '-', '/']))  # 3.0

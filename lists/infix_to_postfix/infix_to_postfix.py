def precedence(op: str) -> int:
    precedence_map = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
        '^': 3,
        '~': 4
    }
    return precedence_map.get(op, 0)


def infix_to_postfix(tokens: list[str]) -> list[str]:
    output = []
    stack = []
    operators = {'+', '-', '*', '/', '^', '~'}

    for token in tokens:
        if token.isdigit():
            # Operand: add to output
            output.append(token)
        elif token == '(':
            # Left parenthesis: push to stack
            stack.append(token)
        elif token == ')':
            # Right parenthesis: pop until '('
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            if stack:
                stack.pop()  # Remove '('
        elif token in operators:
            # Operator: pop higher/equal precedence, then push
            while (stack and stack[-1] != '(' and
                   stack[-1] in operators and
                   precedence(stack[-1]) >= precedence(token)):
                output.append(stack.pop())
            stack.append(token)

    # Pop remaining operators
    while stack:
        output.append(stack.pop())

    return output


if __name__ == "__main__":
    # Test your function
    print(infix_to_postfix(['3', '+', '5', '*', '2']))
    # ['3', '5', '2', '*', '+']

    print(infix_to_postfix(['(', '3', '+', '5', ')', '*', '2']))
    # ['3', '5', '+', '2', '*']

from lists.precedence.precedence import precedence


def infix_to_postfix(tokens: list[str]) -> list[str]:
    output = []
    stack = []
    operators = {"+", "-", "*", "/", "^", "~"}

    for token in tokens:
        if token.isdigit():
            output.append(token)
        elif token == "(":
            stack.append(token)
        elif token == ")":
            while stack and stack[-1] != "(":
                output.append(stack.pop())
            if stack:
                stack.pop()  # discard the '(' rather than sending it to the output
        elif token in operators:
            # Pop operators of higher or equal precedence, then push this one
            while (
                stack
                and stack[-1] != "("
                and stack[-1] in operators
                and precedence(stack[-1]) >= precedence(token)
            ):
                output.append(stack.pop())
            stack.append(token)

    while stack:
        output.append(stack.pop())

    return output


if __name__ == "__main__":
    print(infix_to_postfix(["3", "+", "5", "*", "2"]))
    # ['3', '5', '2', '*', '+']

    print(infix_to_postfix(["(", "3", "+", "5", ")", "*", "2"]))
    # ['3', '5', '+', '2', '*']

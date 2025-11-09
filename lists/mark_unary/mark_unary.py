def mark_unary(tokens: list[str]) -> list[str]:
    result = []
    operators = {'+', '-', '*', '/', '^'}

    for i, token in enumerate(tokens):
        if token == '-':
            # Check if it's unary
            if i == 0 or tokens[i - 1] == '(' or tokens[i - 1] in operators:
                result.append('~')
            else:
                result.append('-')
        else:
            result.append(token)

    return result


if __name__ == "__main__":
    # Test your function
    print(mark_unary(['-', '5', '+', '3']))  # ['~', '5', '+', '3']
    print(mark_unary(['(', '-', '5', ')', '*', '2']))  # ['(', '~', '5', ')', '*', '2']
    print(mark_unary(['3', '-', '5']))  # ['3', '-', '5']

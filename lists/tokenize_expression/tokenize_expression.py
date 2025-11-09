def tokenize_expression(expr: str) -> list[str]:
    expr = expr.replace(" ", "")
    tokens = []
    i = 0

    while i < len(expr):
        if expr[i].isdigit():
            # Accumulate digits for multi-digit numbers
            num = ""
            while i < len(expr) and expr[i].isdigit():
                num += expr[i]
                i += 1
            tokens.append(num)
        else:
            # Operator or parenthesis
            tokens.append(expr[i])
            i += 1

    return tokens


if __name__ == "__main__":
    # Test your function
    print(tokenize_expression("3+5*2"))  # ['3', '+', '5', '*', '2']
    print(tokenize_expression("(10+20)*3"))  # ['(', '10', '+', '20', ')', '*', '3']
    print(tokenize_expression("15 - 7 + 2"))  # ['15', '-', '7', '+', '2']

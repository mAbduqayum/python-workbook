def precedence(operation: str) -> int:
    match operation:
        case '+' | '-':
            return 1
        case '*' | '/':
            return 2
        case '^':
            return 3
        case '~':
            return 4
        case _:
            return -1  # treat -1 as not found


if __name__ == "__main__":
    # Test your function
    print(precedence('+'))  # 1
    print(precedence('-'))  # 1
    print(precedence('*'))  # 2
    print(precedence('/'))  # 2
    print(precedence('^'))  # 3
    print(precedence('~'))  # 4 (unary minus)

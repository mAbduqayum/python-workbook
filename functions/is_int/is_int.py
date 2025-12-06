def is_int(s: str) -> bool:
    if not s:
        return False

    start = 0
    if s[0] in "+-":
        start = 1
        if len(s) == 1:
            return False

    for i in range(start, len(s)):
        if not s[i].isdigit():
            return False

    return True


if __name__ == "__main__":
    # Test your function
    is_int("123")  # True
    is_int("-456")  # True
    is_int("0")  # True
    is_int("12.5")  # False
    is_int("abc")  # False
    is_int("")  # False
    is_int("+789")  # True
    is_int("12a")  # False

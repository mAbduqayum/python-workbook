def password_strength(pwd: str) -> str:
    length = len(pwd)

    has_lower = False
    has_upper = False
    has_digit = False
    has_special = False

    for char in pwd:
        if char.islower():
            has_lower = True
        elif char.isupper():
            has_upper = True
        elif char.isdigit():
            has_digit = True
        elif char in "!@#$%^&*()_+-=[]{}|;:,.<>?":
            has_special = True

    char_types = 0
    if has_lower:
        char_types += 1
    if has_upper:
        char_types += 1
    if has_digit:
        char_types += 1
    if has_special:
        char_types += 1

    if length >= 12 and char_types >= 3:
        return "strong"
    elif length >= 8 and char_types >= 2:
        return "medium"
    else:
        return "weak"


if __name__ == "__main__":
    print(password_strength("abc"))  # "weak"
    print(password_strength("Password1"))  # "medium"
    print(password_strength("P@ssw0rd!"))  # "medium"
    print(password_strength("hello"))  # "weak"
    print(password_strength("Hello123"))  # "medium"

def first_recurring(text: str) -> str | None:
    seen = set()
    for char in text:
        if char in seen:
            return char
        seen.add(char)
    return None


if __name__ == "__main__":
    print(first_recurring("ABCA"))  # "A"
    print(first_recurring("ABCBA"))  # "B"
    print(first_recurring("ABC"))  # None
    print(first_recurring("ABBA"))  # "B"
    print(first_recurring("aAbBaA"))  # "a"
    print(first_recurring(""))  # None

def first_repeat(words: list[str]) -> str:
    seen = set()
    for word in words:
        lower = word.lower()
        if lower in seen:
            return lower
        seen.add(lower)
    return ""


if __name__ == "__main__":
    print(first_repeat(["The", "cat", "saw", "the", "dog"]))  # the
    print(first_repeat(["red", "blue", "green", "blue", "red"]))  # blue
    print(first_repeat(["one", "two", "three"]))  # ""

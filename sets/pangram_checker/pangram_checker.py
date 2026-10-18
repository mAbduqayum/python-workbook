import string


def is_pangram(text: str) -> bool:
    alphabet = set(string.ascii_lowercase)
    return set(text.lower()) >= alphabet


if __name__ == "__main__":
    print(is_pangram("The quick brown fox jumps over the lazy dog"))  # True
    print(is_pangram("Hello World"))  # False
    print(is_pangram("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))  # True

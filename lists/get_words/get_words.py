def get_words(sentence: str) -> list[str]:
    if not sentence:
        return []
    return sentence.split()


if __name__ == "__main__":
    # Test your function
    print(get_words("Hello world"))  # ["Hello", "world"]
    print(get_words("Python is fun"))  # ["Python", "is", "fun"]
    print(get_words(""))  # []

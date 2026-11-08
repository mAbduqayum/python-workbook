def distinct_words(text: str) -> int:
    words = set()
    for word in text.split():
        words.add(word.lower())
    return len(words)


if __name__ == "__main__":
    print(distinct_words("the cat and the hat"))  # 4
    print(distinct_words("The the THE"))  # 1
    print(distinct_words(""))  # 0

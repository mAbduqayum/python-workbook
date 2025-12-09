def word_frequency(file_path: str) -> dict[str, int]:
    freq = {}
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            words = line.split()
            for word in words:
                # Remove punctuation and convert to lowercase
                clean_word = word.lower().strip(".,!?;:'\"")
                if clean_word:
                    if clean_word in freq:
                        freq[clean_word] = freq[clean_word] + 1
                    else:
                        freq[clean_word] = 1
    return freq


def word_frequency2(file_path: str) -> dict[str, int]:
    from collections import Counter

    words = []
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            for word in line.split():
                # Remove punctuation and convert to lowercase
                clean_word = word.lower().strip(".,!?;:'\"")
                if clean_word:
                    words.append(clean_word)

    return dict(Counter(words))


if __name__ == "__main__":
    # Create a test file
    with open("text.txt", "w") as f:
        f.write("Hello world!\n")
        f.write("hello Python, world.\n")

    # Test your functions
    print(word_frequency("text.txt"))  # {'hello': 2, 'world': 2, 'python': 1}
    print(word_frequency2("text.txt"))  # {'hello': 2, 'world': 2, 'python': 1}

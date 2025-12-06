def find_repeated_words(file_path: str) -> list[tuple[int, str]]:
    repeats = []
    prev_word = None
    with open(file_path, "r", encoding="utf-8") as f:
        for line_num, line in enumerate(f, 1):
            words = line.split()
            for word in words:
                word_lower = word.lower().strip(".,!?;:'\"")
                if prev_word and word_lower == prev_word:
                    repeats.append((line_num, word_lower))
                prev_word = word_lower
    return repeats


if __name__ == "__main__":
    # Create a test file
    with open("sample.txt", "w") as f:
        f.write("The the quick brown fox\n")
        f.write("jumped over over the\n")
        f.write("the lazy dog.\n")

    # Test your function
    repeats = find_repeated_words("sample.txt")
    for line_num, word in repeats:
        print(f"Line {line_num}: '{word}' is repeated")

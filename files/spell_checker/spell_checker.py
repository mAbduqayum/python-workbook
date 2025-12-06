def spell_checker(file_path: str, dictionary_path: str) -> list[str]:
    # Load dictionary
    dictionary = set()
    with open(dictionary_path, "r", encoding="utf-8") as f:
        for line in f:
            word = line.strip().lower()
            if word:
                dictionary.add(word)

    # Check text file
    misspelled = set()
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            words = line.split()
            for word in words:
                # Remove punctuation
                clean_word = word.lower().strip(".,!?;:'\"")
                if clean_word and clean_word not in dictionary:
                    misspelled.add(clean_word)

    return sorted(list(misspelled))


if __name__ == "__main__":
    # Create a dictionary file
    with open("dictionary.txt", "w") as f:
        f.write("hello\nworld\npython\ncode\n")

    # Create a text file to check
    with open("text.txt", "w") as f:
        f.write("Hello world! This is pyton code.\n")
        f.write("Some wrng words here.\n")

    # Test your function
    misspelled = spell_checker("text.txt", "dictionary.txt")
    print(f"Misspelled words: {misspelled}")

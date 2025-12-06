def six_vowel_words(file_path: str) -> list[str]:
    result = []
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            word = line.strip()
            if has_six_vowels_in_order(word):
                result.append(word)
    return result


def has_six_vowels_in_order(word: str) -> bool:
    vowels = "aeiouy"
    word_lower = word.lower()
    vowel_index = 0

    for char in word_lower:
        if vowel_index < len(vowels) and char == vowels[vowel_index]:
            vowel_index += 1
        elif char in vowels:
            # Found a vowel out of order or duplicate
            return False

    return vowel_index == len(vowels)


if __name__ == "__main__":
    # Create a test file
    with open("words.txt", "w") as f:
        f.write("facetiously\n")
        f.write("abstentiously\n")
        f.write("adventitiously\n")
        f.write("hello\n")
        f.write("world\n")

    # Test your function
    words = six_vowel_words("words.txt")
    print(f"Found {len(words)} words with six vowels in order:")
    for word in words:
        print(f"  {word}")

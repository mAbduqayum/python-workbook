def word_frequency(file_path: str) -> dict[str, int]:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    freq: dict[str, int] = {}
    for word in content.split():
        freq[word] = freq.get(word, 0) + 1
    return freq


if __name__ == "__main__":
    # Create a test file
    with open("text.txt", "w") as f:
        f.write("hello world\n")
        f.write("hello python world\n")

    # Test your function
    print(word_frequency("text.txt"))

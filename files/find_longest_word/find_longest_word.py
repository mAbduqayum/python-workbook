def find_longest_word(file_path: str) -> str:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    words = content.split()
    return max(words, key=len)


if __name__ == "__main__":
    # Create a test file
    with open("text.txt", "w") as f:
        f.write("The quick brown fox jumps over the lazy dog\n")
        f.write("Python programming is wonderful\n")

    # Test your function
    print(find_longest_word("text.txt"))  # "programming"

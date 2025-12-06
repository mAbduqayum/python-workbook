def letter_frequency(file_path: str) -> dict[str, int]:
    freq = {}
    with open(file_path, "r", encoding="utf-8") as f:
        for char in f.read():
            if char.isalpha():
                char = char.lower()
                freq[char] = freq.get(char, 0) + 1
    return freq


if __name__ == "__main__":
    # Create a test file
    with open("sample.txt", "w") as f:
        f.write("Hello World!\n")
        f.write("Python is great.\n")

    # Test your function
    freq = letter_frequency("sample.txt")
    for letter, count in sorted(freq.items()):
        print(f"{letter}: {count}")

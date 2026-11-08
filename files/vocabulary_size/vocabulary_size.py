def vocabulary_size(file_path: str) -> int:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    words = set()
    for word in content.split():
        words.add(word.lower())
    return len(words)


if __name__ == "__main__":
    with open("text.txt", "w") as f:
        f.write("The cat and the hat\n")
        f.write("The end\n")

    print(vocabulary_size("text.txt"))  # 5

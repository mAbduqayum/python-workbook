def count_words(file_path: str) -> int:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    return len(content.split())


if __name__ == "__main__":
    with open("text.txt", "w") as f:
        f.write("Hello world\n")
        f.write("This is a test file\n")

    print(count_words("text.txt"))  # 7

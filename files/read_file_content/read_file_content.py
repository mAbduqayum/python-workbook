def read_file_content(file_path: str) -> str:
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()


if __name__ == "__main__":
    # Create a test file
    with open("test.txt", "w") as f:
        f.write("Hello, World!\nThis is a test file.")

    # Test your function
    print(read_file_content("test.txt"))

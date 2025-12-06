def count_lines(file_path: str) -> int:
    with open(file_path, "r", encoding="utf-8") as f:
        return len(f.readlines())


if __name__ == "__main__":
    # Create a test file
    with open("test.txt", "w") as f:
        f.write("Line 1\nLine 2\nLine 3\n")

    # Test your function
    print(count_lines("test.txt"))  # 3

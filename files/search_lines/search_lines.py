def search_lines(file_path: str, term: str) -> list[tuple[int, str]]:
    results: list[tuple[int, str]] = []
    with open(file_path, "r", encoding="utf-8") as f:
        for line_num, line in enumerate(f, 1):
            if term in line:
                results.append((line_num, line.rstrip("\n")))
    return results


if __name__ == "__main__":
    # Create a test file
    with open("code.txt", "w") as f:
        f.write("def hello():\n")
        f.write("    print('Hello')\n")
        f.write("def goodbye():\n")
        f.write("    print('Goodbye')\n")

    # Test your function
    print(search_lines("code.txt", "def"))

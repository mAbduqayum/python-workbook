def write_lines(file_path: str, lines: list[str]) -> None:
    with open(file_path, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line + "\n")


if __name__ == "__main__":
    write_lines("output.txt", ["apple", "banana", "cherry"])

    # Verify by reading the file
    with open("output.txt", "r") as f:
        print(f.read())

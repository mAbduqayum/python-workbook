def append_line(file_path: str, line: str) -> None:
    with open(file_path, "a", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    with open("log.txt", "w") as f:
        f.write("Entry 1\n")

    append_line("log.txt", "Entry 2")
    append_line("log.txt", "Entry 3")

    with open("log.txt", "r") as f:
        print(f.read())

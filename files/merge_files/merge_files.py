def merge_files(file_paths: list[str], output_path: str) -> None:
    with open(output_path, "w", encoding="utf-8") as outfile:
        for file_path in file_paths:
            with open(file_path, "r", encoding="utf-8") as infile:
                outfile.write(infile.read())


if __name__ == "__main__":
    # Create test files
    with open("file1.txt", "w") as f:
        f.write("Content of file 1\n")
    with open("file2.txt", "w") as f:
        f.write("Content of file 2\n")
    with open("file3.txt", "w") as f:
        f.write("Content of file 3\n")

    # Merge files
    merge_files(["file1.txt", "file2.txt", "file3.txt"], "merged.txt")

    # Verify
    with open("merged.txt", "r") as f:
        print(f.read())

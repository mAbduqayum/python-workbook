def remove_comments(input_path: str, output_path: str) -> int:
    removed = 0
    with open(input_path, "r", encoding="utf-8") as infile:
        with open(output_path, "w", encoding="utf-8") as outfile:
            for line in infile:
                if line.lstrip().startswith("#"):
                    removed += 1
                else:
                    outfile.write(line)
    return removed


if __name__ == "__main__":
    # Create a test file
    with open("code.py", "w") as f:
        f.write("# This is a comment\n")
        f.write("x = 1\n")
        f.write("  # Indented comment\n")
        f.write("y = 2  # inline comment stays\n")

    # Test your function
    removed = remove_comments("code.py", "clean_code.py")
    print(f"Removed {removed} comment lines")

    # Verify output
    with open("clean_code.py", "r") as f:
        print(f.read())

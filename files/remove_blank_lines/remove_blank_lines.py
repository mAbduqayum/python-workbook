def remove_blank_lines(input_path: str, output_path: str) -> int:
    removed = 0
    with open(input_path, "r", encoding="utf-8") as infile:
        with open(output_path, "w", encoding="utf-8") as outfile:
            for line in infile:
                if line.strip():
                    outfile.write(line)
                else:
                    removed += 1
    return removed


if __name__ == "__main__":
    # Create a test file with blank lines
    with open("input.txt", "w") as f:
        f.write("Line 1\n")
        f.write("\n")
        f.write("Line 2\n")
        f.write("   \n")
        f.write("Line 3\n")

    # Test your function
    removed = remove_blank_lines("input.txt", "output.txt")
    print(f"Removed {removed} blank lines")

    # Verify output
    with open("output.txt", "r") as f:
        print(f.read())

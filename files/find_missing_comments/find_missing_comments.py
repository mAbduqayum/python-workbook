def find_missing_comments(file_path: str) -> list[list[int | str]]:
    missing = []
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    for i, line in enumerate(lines, 1):
        if line.strip().startswith("def "):
            # Extract function name
            func_name = line.strip()[4:].split("(")[0]

            # Check previous non-empty line for comment
            has_comment = False
            for j in range(i - 2, -1, -1):  # i-2 because i is 1-indexed
                prev_line = lines[j].strip()
                if prev_line:  # First non-empty line
                    if "#" in prev_line:
                        has_comment = True
                    break

            if not has_comment:
                missing.append([i, func_name])

    return missing


if __name__ == "__main__":
    # Create a test Python file
    with open("code.py", "w") as f:
        f.write("# This is documented\n")
        f.write("def good_function():\n")
        f.write("    pass\n")
        f.write("\n")
        f.write("def bad_function():\n")
        f.write("    pass\n")

    # Test your function
    missing = find_missing_comments("code.py")
    for line_num, func_name in missing:
        print(f"Line {line_num}: {func_name} has no comment")

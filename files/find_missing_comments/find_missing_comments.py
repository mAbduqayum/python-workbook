def has_preceding_comment(lines: list[str], def_index: int) -> bool:
    for j in range(def_index - 1, -1, -1):
        prev_line = lines[j].strip()
        if prev_line:
            return "#" in prev_line
    return False


def find_missing_comments(file_path: str) -> list[list[int | str]]:
    missing = []
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    for line_number, line in enumerate(lines, 1):
        if line.strip().startswith("def "):
            func_name = line.strip().removeprefix("def ").split("(")[0]
            if not has_preceding_comment(lines, line_number - 1):
                missing.append([line_number, func_name])

    return missing


if __name__ == "__main__":
    with open("code.py", "w") as f:
        f.write("# This is documented\n")
        f.write("def good_function():\n")
        f.write("    pass\n")
        f.write("\n")
        f.write("def bad_function():\n")
        f.write("    pass\n")

    missing = find_missing_comments("code.py")
    for line_num, func_name in missing:
        print(f"Line {line_num}: {func_name} has no comment")

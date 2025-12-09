# Find Missing Comments

Create a function that finds Python functions without preceding comment lines.

## Template

```python
def find_missing_comments(file_path: str) -> list[tuple[int, str]]:
    pass


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
```

## Note

- Find all lines starting with `def ` (function definitions)
- Check if the previous non-empty line contains a comment (`#`)
- Return list of tuples: (line_number, function_name)
- Extract just the function name (without `def`, parameters, or colon)
- Skip the first line of the file (if it's a function definition, it can't have a preceding comment)

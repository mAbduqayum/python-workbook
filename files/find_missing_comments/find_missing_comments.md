# Find Missing Comments

Create a function that finds Python functions without preceding comment lines.

## Template

```python
def find_missing_comments(file_path: str) -> list[list[int | str]]:
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

- A function definition is a line starting with `def `
- A function counts as documented when the nearest non-empty line above it contains a `#`
- Return a list of lists: [line_number, function_name], using the line number of the `def` line
- Report just the function name (without `def`, parameters, or colon)
- A definition on the first line of the file has no line above it, so it is always reported

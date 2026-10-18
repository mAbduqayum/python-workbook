# Remove Comments

Create a function that removes Python comment lines from a file.

## Template

```python
def remove_comments(input_path: str, output_path: str) -> int:
    pass


if __name__ == "__main__":
    # Create a test file
    with open("code.py", "w") as f:
        f.write("# This is a comment\n")
        f.write("x = 1\n")
        f.write("  # Indented comment\n")
        f.write("y = 2  # inline comment stays\n")

    # Test your function
    print(remove_comments("code.py", "clean_code.py"))  # 2

    # Verify output
    with open("clean_code.py", "r") as f:
        print(f.read())
    # Output:
    # x = 1
    # y = 2  # inline comment stays
```

## Note

- Remove lines where the first non-whitespace character is `#`
- Keep lines with inline comments (e.g., `x = 1  # comment`)
- Return the count of removed lines
- Preserve original indentation of non-comment lines

# Remove Blank Lines

Create a function that reads a file and writes its content to a new file with all blank lines removed.

## Template

```python
def remove_blank_lines(input_path: str, output_path: str) -> int:
    pass


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
    print(f"Removed {removed} blank lines")  # Removed 2 blank lines

    # Verify output
    with open("output.txt", "r") as f:
        print(f.read())
```

## Note

- A blank line is a line that is empty or contains only whitespace
- Return the number of blank lines that were removed
- Preserve the content of non-blank lines exactly (including trailing spaces)

# Append Line

Create a function that appends a single line to a file.

## Template

```python
def append_line(file_path: str, line: str) -> None:
    pass


if __name__ == "__main__":
    # Create initial file
    with open("log.txt", "w") as f:
        f.write("Entry 1\n")

    # Append a new line
    append_line("log.txt", "Entry 2")

    # Verify
    with open("log.txt", "r") as f:
        print(f.read())
    # Output:
    # Entry 1
    # Entry 2
```

## Note

- The appended line ends with a newline character; existing content is untouched
- If the file doesn't exist, it should be created

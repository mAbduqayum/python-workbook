# Write Lines

Create a function that writes a list of strings to a file, with each string on a new line.

## Template

```python
def write_lines(file_path: str, lines: list[str]) -> None:
    pass


if __name__ == "__main__":
    write_lines("output.txt", ["apple", "banana", "cherry"])

    # Verify by reading the file
    with open("output.txt", "r") as f:
        print(f.read())
    # Output:
    # apple
    # banana
    # cherry
```

## Note

- Each string is followed by a newline character, including the last one
- The function creates a new file or overwrites an existing one

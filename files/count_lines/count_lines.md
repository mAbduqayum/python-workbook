# Count Lines

Create a function that counts the number of lines in a text file.

## Template

```python
def count_lines(file_path: str) -> int:
    pass


if __name__ == "__main__":
    # Create a test file
    with open("test.txt", "w") as f:
        f.write("Line 1\nLine 2\nLine 3\n")

    # Test your function
    print(count_lines("test.txt"))  # 3
```

## Note

- An empty file has 0 lines
- A final line without a trailing newline still counts: a file with just "hello" has 1 line

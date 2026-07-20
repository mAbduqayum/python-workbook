# Head

Create a function that prints the first n lines of a file, similar to the Unix `head` command.

## Template

```python
def head(file_path: str, n: int = 10) -> None:
    pass


if __name__ == "__main__":
    # Test with sample files
    head("../samples/poem.txt", 3)
    # Roses are red,
    # Violets are blue,
    # Python is great,
```

## Note

- Print each line without the trailing newline character
- If the file has fewer than n lines, print all lines

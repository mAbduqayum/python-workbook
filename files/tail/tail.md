# Tail

Create a function that prints the last n lines of a file, similar to the Unix `tail` command.

## Template

```python
def tail(file_path: str, n: int = 10) -> None:
    pass


if __name__ == "__main__":
    # Test with sample files
    tail("../samples/poem.txt", 2)
    # Python is great,
    # And so are you!
```

## Note

- Print each line without the trailing newline character
- If the file has fewer than n lines, print all lines
- Default value for n is 10
- Test with different sample files: `../samples/khayyam.txt` (UTF-8), `../samples/server_log.txt`

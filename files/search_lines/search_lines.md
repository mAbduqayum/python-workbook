# Search Lines

Create a function that finds all lines containing a search term and returns them with their line numbers.

## Template

```python
def search_lines(file_path: str, term: str) -> list[list[int | str]]:
    pass


if __name__ == "__main__":
    # Create a test file
    with open("code.txt", "w") as f:
        f.write("def hello():\n")
        f.write("    print('Hello')\n")
        f.write("def goodbye():\n")
        f.write("    print('Goodbye')\n")

    # Test your function
    print(search_lines("code.txt", "def"))
    # [(1, "def hello():"), (3, "def goodbye():")]
```

## Note

- Line numbers start at 1
- The search is case-sensitive
- Return lines without the trailing newline character
- Return an empty list if no matches are found

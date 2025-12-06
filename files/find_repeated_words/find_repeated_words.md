# Find Repeated Words

Create a function that finds consecutively repeated words in a file.

## Template

```python
def find_repeated_words(file_path: str) -> list[tuple[int, str]]:
    pass


if __name__ == "__main__":
    # Create a test file
    with open("sample.txt", "w") as f:
        f.write("The the quick brown fox\n")
        f.write("jumped over over the\n")
        f.write("the lazy dog.\n")

    # Test your function
    repeats = find_repeated_words("sample.txt")
    for line_num, word in repeats:
        print(f"Line {line_num}: '{word}' is repeated")
```

## Note

- A repeated word appears twice in a row (e.g., "the the")
- Comparison should be case-insensitive ("The the" counts as repeated)
- Check across line boundaries (word at end of line followed by same word at start of next line)
- Return list of tuples: (line_number, word) where line_number is where the second occurrence appears
- The word in the tuple should be lowercase

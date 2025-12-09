# Spell Checker

Create a function that checks spelling against a dictionary file.

## Template

```python
def spell_checker(file_path: str, dictionary_path: str) -> list[str]:
    pass


if __name__ == "__main__":
    # Create a dictionary file
    with open("dictionary.txt", "w") as f:
        f.write("hello\nworld\npython\ncode\n")

    # Create a text file to check
    with open("text.txt", "w") as f:
        f.write("Hello world! This is pyton code.\n")
        f.write("Some wrng words here.\n")

    # Test your function
    misspelled = spell_checker("text.txt", "dictionary.txt")
    print(f"Misspelled words: {misspelled}")
```

## Note

- The dictionary file contains one valid word per line
- Check all words in the text file against the dictionary
- Comparison should be case-insensitive
- Strip punctuation from words before checking (.,!?;:'")
- Return a list of unique misspelled words (no duplicates)
- Return words in lowercase
- Empty words (after stripping punctuation) should be ignored

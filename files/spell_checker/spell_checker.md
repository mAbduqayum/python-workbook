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
        f.write("Helo world, pyton code! Helo!\n")

    # Test your function
    print(spell_checker("text.txt", "dictionary.txt"))  # ['helo', 'pyton']
```

## Note

- The dictionary file contains one valid word per line
- Comparison is case-insensitive
- Strip punctuation from words before checking (.,!?;:'")
- Return a list of unique misspelled words (no duplicates), in lowercase
- Tokens that are only punctuation are ignored

# Vocabulary Size

Create a function that counts how many different words a file uses.

You counted the different words in a string in [Distinct Words](../../sets/distinct_words/distinct_words.md); now count them in a file.

## Template

```python
def vocabulary_size(file_path: str) -> int:
    pass


if __name__ == "__main__":
    # Create a test file
    with open("text.txt", "w") as f:
        f.write("The cat and the hat\n")
        f.write("The end\n")

    # Test your function
    print(vocabulary_size("text.txt"))  # 5
```

## Note

- Case doesn't matter: `The` and `the` are the same word
- An empty file has 0 words

# Word Frequency

Create a function that counts the frequency of each word in a file and returns a dictionary.

## Template

```python
def word_frequency(file_path: str) -> dict[str, int]:
    pass


if __name__ == "__main__":
    # Create a test file
    with open("text.txt", "w") as f:
        f.write("Hello world!\n")
        f.write("hello Python, world.\n")

    # Test your function
    print(word_frequency("text.txt"))
    # {'hello': 2, 'world': 2, 'python': 1}
```

## Note

- Words are separated by whitespace
- Words are case-insensitive ("Hello" and "hello" are the same)
- Strip common punctuation (.,!?;:'") from words
- Return an empty dictionary for an empty file
- After cleaning, skip empty strings

## Bonus Challenge

Implement `word_frequency2` using Python's `Counter` from the `collections` module

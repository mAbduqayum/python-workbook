# Count Words

Create a function that counts the total number of words in a file.

## Template

```python
def count_words(file_path: str) -> int:
    pass


if __name__ == "__main__":
    # Create a test file
    with open("text.txt", "w") as f:
        f.write("Hello world\n")
        f.write("This is a test file\n")

    # Test your function
    print(count_words("text.txt"))  # 7
```

## Note

- Words are separated by whitespace
- An empty file has 0 words
- Multiple spaces between words should not affect the count

# Find Longest Word

Create a function that finds the longest word in a file.

## Template

```python
def find_longest_word(file_path: str) -> str:
    pass


if __name__ == "__main__":
    # Create a test file
    with open("text.txt", "w") as f:
        f.write("The quick brown fox jumps over the lazy dog\n")
        f.write("Python programming is wonderful\n")

    # Test your function
    print(find_longest_word("text.txt"))  # "programming"
```

## Note

- Words are separated by whitespace
- If there are multiple words with the same longest length, return the first one
- Assume the file is not empty and contains at least one word

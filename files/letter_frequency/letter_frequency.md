# Letter Frequency

Create a function that counts the frequency of each letter in a file.

## Template

```python
def letter_frequency(file_path: str) -> dict[str, int]:
    pass


if __name__ == "__main__":
    # Create a test file
    with open("sample.txt", "w") as f:
        f.write("Hello World!\n")

    # Test your function
    print(letter_frequency("sample.txt"))
    # {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}
```

## Note

- Count only alphabetic characters, case-insensitively: keys are lowercase letters
- Return an empty dictionary for empty files or files with no letters

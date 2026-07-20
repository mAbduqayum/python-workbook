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
        f.write("Python is great.\n")

    # Test your function
    freq = letter_frequency("sample.txt")
    for letter, count in sorted(freq.items()):
        print(f"{letter}: {count}")
```

## Note

- Count only alphabetic characters, case-insensitively: keys are lowercase letters
- Return an empty dictionary for empty files or files with no letters

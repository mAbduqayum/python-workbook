# Redact Text

Create a function that replaces sensitive words with asterisks in a file.

## Template

```python
def redact_text(input_path: str, words_path: str, output_path: str) -> int:
    pass


if __name__ == "__main__":
    # Create a sensitive words file
    with open("sensitive.txt", "w") as f:
        f.write("secret\npassword\nconfidential\n")

    # Create a text file
    with open("document.txt", "w") as f:
        f.write("This is a secret document.\n")
        f.write("The password is hidden.\n")
        f.write("Public information here.\n")

    # Test your function
    count = redact_text("document.txt", "sensitive.txt", "redacted.txt")
    print(f"Redacted {count} words")

    # View redacted file
    with open("redacted.txt", "r") as f:
        print(f.read())
```

## Note

- Read sensitive words from words_path (one word per line)
- Replace each occurrence of sensitive words with asterisks (same length as the word)
- Matching should be case-insensitive
- Preserve the original case pattern in the replacement (if "Secret" is redacted, output "******")
- Return the total count of redacted words
- Preserve all punctuation and whitespace

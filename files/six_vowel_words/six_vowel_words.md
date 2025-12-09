# Six Vowel Words

Create a function that finds words containing the vowels A, E, I, O, U, Y in that exact order.

## Template

```python
def six_vowel_words(file_path: str) -> list[str]:
    pass


if __name__ == "__main__":
    # Create a test file
    with open("words.txt", "w") as f:
        f.write("facetiously\n")
        f.write("abstentiously\n")
        f.write("adventitiously\n")
        f.write("hello\n")
        f.write("world\n")

    # Test your function
    words = six_vowel_words("words.txt")
    print(f"Found {len(words)} words with six vowels in order:")
    for word in words:
        print(f"  {word}")
```

## Note

- Each vowel (a, e, i, o, u, y) must appear exactly once in the word
- The vowels must appear in alphabetical order (a before e before i, etc.)
- Other letters can appear between the vowels
- Comparison should be case-insensitive
- Each line in the file contains one word
- Return words in the order they appear in the file

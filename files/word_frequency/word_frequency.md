# Word Frequency

Create a function that counts the frequency of each word in a file and returns a dictionary.

## Template

```python
def word_frequency(file_path: str) -> dict[str, int]:
    pass


if __name__ == "__main__":
    # Create a test file
    with open("text.txt", "w") as f:
        f.write("hello world\n")
        f.write("hello python world\n")

    # Test your function
    print(word_frequency("text.txt"))
    # {'hello': 2, 'world': 2, 'python': 1}
```

## Note

- Words are separated by whitespace
- Words are case-sensitive ("Hello" and "hello" are different)
- Return an empty dictionary for an empty file

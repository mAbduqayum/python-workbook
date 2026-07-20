# Read File Content

Create a function that reads the entire content of a text file and returns it as a string.

## Template

```python
def read_file_content(file_path: str) -> str:
    pass


if __name__ == "__main__":
    # Create a test file
    with open("test.txt", "w") as f:
        f.write("Hello, World!\nThis is a test file.")

    # Test your function
    print(read_file_content("test.txt"))
    # Output: Hello, World!
    #         This is a test file.
```

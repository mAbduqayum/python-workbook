# Merge Files

Create a function that merges multiple text files into one output file.

## Template

```python
def merge_files(file_paths: list[str], output_path: str) -> None:
    pass


if __name__ == "__main__":
    # Create test files
    with open("file1.txt", "w") as f:
        f.write("Content of file 1\n")
    with open("file2.txt", "w") as f:
        f.write("Content of file 2\n")
    with open("file3.txt", "w") as f:
        f.write("Content of file 3\n")

    # Merge files
    merge_files(["file1.txt", "file2.txt", "file3.txt"], "merged.txt")

    # Verify
    with open("merged.txt", "r") as f:
        print(f.read())
```

## Note

- Files are merged in the order they appear in the list
- The content of each file is written exactly as-is
- If a file doesn't end with a newline, the next file's content follows immediately

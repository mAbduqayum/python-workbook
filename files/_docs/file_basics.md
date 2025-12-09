# File Basics

## Opening Files

Use the `open()` function to open a file:

```python
file = open("example.txt", "r", encoding="utf-8")
content = file.read()
file.close()
```

### File Modes

| Mode | Description |
|------|-------------|
| `'r'` | Read (default) - file must exist |
| `'w'` | Write - creates new or truncates existing |
| `'a'` | Append - creates new or appends to existing |
| `'x'` | Exclusive create - fails if file exists |

## Context Managers

Always use `with` statement to automatically close files:

```python
with open("example.txt", "r", encoding="utf-8") as file:
    content = file.read()
# file is automatically closed here
```

## Reading Files

### Read entire file

```python
with open("file.txt", "r", encoding="utf-8") as f:
    content = f.read()  # Returns entire file as string
```

### Read line by line

```python
with open("file.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())  # strip() removes trailing newline
```

### Read all lines as list

```python
with open("file.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()  # Returns list of lines (with newlines)
```

### Read single line

```python
with open("file.txt", "r", encoding="utf-8") as f:
    first_line = f.readline()  # Returns first line
    second_line = f.readline()  # Returns second line
```

## Writing Files

### Write string to file

```python
with open("file.txt", "w", encoding="utf-8") as f:
    f.write("Hello, World!\n")
```

### Write multiple lines

```python
lines = ["line 1", "line 2", "line 3"]
with open("file.txt", "w", encoding="utf-8") as f:
    for line in lines:
        f.write(line + "\n")
```

Or using `writelines()` (note: doesn't add newlines automatically):

```python
lines = ["line 1\n", "line 2\n", "line 3\n"]
with open("file.txt", "w", encoding="utf-8") as f:
    f.writelines(lines)
```

## Appending to Files

```python
with open("file.txt", "a", encoding="utf-8") as f:
    f.write("New line at the end\n")
```

## Encoding

Always specify `encoding="utf-8"` for text files to ensure consistent behavior across platforms:

```python
with open("file.txt", "r", encoding="utf-8") as f:
    content = f.read()
```

## Common Patterns

### Count lines in a file

```python
with open("file.txt", "r", encoding="utf-8") as f:
    line_count = sum(1 for _ in f)
```

### Process each line

```python
with open("file.txt", "r", encoding="utf-8") as f:
    for line_num, line in enumerate(f, 1):
        print(f"{line_num}: {line.strip()}")
```

### Copy file content

```python
with open("source.txt", "r", encoding="utf-8") as src:
    with open("dest.txt", "w", encoding="utf-8") as dst:
        dst.write(src.read())
```

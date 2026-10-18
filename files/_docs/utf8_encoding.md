# UTF-8 Explained Simply

## What is UTF-8?

UTF-8 is a way to turn text into numbers that computers can store and
understand.

Think of it like this: computers only understand numbers (specifically 0s and
1s). So we need a "translation system" to convert letters, symbols, and emojis
into numbers. UTF-8 is that translation system.

### Why "UTF-8"?

- **UTF** = Unicode Transformation Format
- **8** = it uses 8-bit chunks (bytes) as building blocks

### The Clever Part

UTF-8 is smart about space:

| Character Type        | Bytes Used | Examples      |
|-----------------------|------------|---------------|
| Basic English letters | 1 byte     | A, B, z, 1, @ |
| Accented letters      | 2 bytes    | é, ñ, ü       |
| Asian characters      | 3 bytes    | 中, 日, 한    |
| Emojis                | 4 bytes    | 😀, 🎉, 🐍    |

This means English text stays small, while still supporting every language and
symbol in the world.

---

## UTF-8 in Python

### Python Strings Are Unicode

Good news! Inside your program, a Python string can hold any character from
any language, emojis included:

```python
message = "Hello, 世界! 🐍"
print(message)  # Output: Hello, 世界! 🐍
```

UTF-8 only comes into play when text leaves your program as **bytes**: when
it is saved to a file or sent over the internet.

### Encoding: Text → Bytes

When you need to save text to a file or send it over the internet, you convert
it to bytes:

```python
text = "Hello, 世界!"

# Convert string to bytes
encoded = text.encode('utf-8')
print(encoded)  # b'Hello, \xe4\xb8\x96\xe7\x95\x8c!'
print(type(encoded))  # <class 'bytes'>
```

### Decoding: Bytes → Text

When you receive bytes and want readable text:

```python
byte_data = b'Hello, \xe4\xb8\x96\xe7\x95\x8c!'

# Convert bytes back to string
decoded = byte_data.decode('utf-8')
print(decoded)  # Hello, 世界!
```

### Reading and Writing Files

Always specify encoding when working with files. Without it, `open()` uses
your operating system's default encoding, which is not UTF-8 everywhere
(Windows often uses a different one). The same code could then read a file
correctly on one computer and fail on another.

```python
# Writing
with open('myfile.txt', 'w', encoding='utf-8') as f:
    f.write("Hello, 世界! 🎉")

# Reading
with open('myfile.txt', 'r', encoding='utf-8') as f:
    content = f.read()
```

### Common Gotcha: The UnicodeDecodeError

If you see this error, it usually means:

1. The file isn't actually UTF-8 encoded
2. You forgot to specify the encoding, and your system's default doesn't
   match the file

```python
# This fails if the file uses a different encoding
with open('oldfile.txt', 'r', encoding='utf-8') as f:
    content = f.read()  # UnicodeDecodeError!

# If you know the file's real encoding, use that instead
with open('oldfile.txt', 'r', encoding='latin-1') as f:
    content = f.read()
```

> **Note:** `latin-1` never raises an error, because every byte is some
> character in it. If you pick it for a file that isn't really `latin-1`,
> you get garbled text instead of an error, so check that the result looks
> right.

---

## Quick Reference

| Task             | Code                                |
|------------------|-------------------------------------|
| String to bytes  | `"text".encode('utf-8')`            |
| Bytes to string  | `b"bytes".decode('utf-8')`          |
| Read UTF-8 file  | `open(file, 'r', encoding='utf-8')` |
| Write UTF-8 file | `open(file, 'w', encoding='utf-8')` |

---

## Key Takeaways

1. **UTF-8** is the most popular way to represent text as numbers
2. **Python strings** hold Unicode text; UTF-8 is how that text is stored as
   bytes
3. **Always specify `encoding='utf-8'`** when reading/writing files
4. Use `.encode()` to go from text → bytes
5. Use `.decode()` to go from bytes → text

That's it! UTF-8 lets your Python code work with any language or emoji in the
world. 🌍
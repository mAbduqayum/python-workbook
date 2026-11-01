# Repetition in Python - Strings in Loops

A string is a sequence of characters, so a loop can visit them by position and
build a new string one piece at a time.

## Indexing

Every character has an **index**. The first is at index `0`, and negative
indexes count from the end:

```python
word = "python"
print(word[0])  # p
print(word[2])  # t
print(word[-1])  # n
print(word[-2])  # o
```

## Looping by Index

Looping over `range(len(word))` gives you each position, which lets you compare
a character with another one:

```python
word = "hello"
for i in range(len(word) - 1):
    if word[i] == word[i + 1]:
        print(f"Double letter: {word[i]}")  # Double letter: l
```

## Building a String

Start from the empty string `""`. Adding to the end keeps the order, and adding
to the front reverses it:

```python
shouted = ""
backward = ""
for char in "hello":
    shouted += char.upper()
    backward = char + backward
print(shouted)  # HELLO
print(backward)  # olleh
```

## Numbers in Strings

`+` can't join a string and a number. Convert the number with `str()` first:

```python
digits = ""
for i in range(1, 6):
    digits += str(i)
print(digits)  # 12345
```

## Upper and Lower Case

`.isupper()` and `.islower()` check a letter's case. Both return `False` for
digits, spaces and punctuation:

```python
upper = 0
lower = 0
for char in "Hello, World!":
    if char.isupper():
        upper += 1
    elif char.islower():
        lower += 1
print(upper, lower)  # 2 8
```

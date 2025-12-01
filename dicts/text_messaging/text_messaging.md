# Text Messaging (T9)

Convert a message to old cellphone key presses.

## Task

Write a function `text_messaging(message)` that converts a text message to the sequence of key presses needed on an old
cellphone keypad (T9 style).

- Convert message to uppercase before processing
- Each letter requires pressing its key 1-4 times
- Spaces are represented by '0'
- Include punctuation: . , ? ! :
- Skip characters that don't have a mapping
- Return empty string for empty input

### T9 Keypad Layout

| Key | Symbols | Key | Symbols |
|-----|---------|-----|---------|
| 1   | .,?!:   | 6   | MNO     |
| 2   | ABC     | 7   | PQRS    |
| 3   | DEF     | 8   | TUV     |
| 4   | GHI     | 9   | WXYZ    |
| 5   | JKL     | 0   | space   |

## Template

```python
T9_KEYPAD = {
    'A': '2', 'B': '22', 'C': '222',
    'D': '3', 'E': '33', 'F': '333',
    'G': '4', 'H': '44', 'I': '444',
    'J': '5', 'K': '55', 'L': '555',
    'M': '6', 'N': '66', 'O': '666',
    'P': '7', 'Q': '77', 'R': '777', 'S': '7777',
    'T': '8', 'U': '88', 'V': '888',
    'W': '9', 'X': '99', 'Y': '999', 'Z': '9999',
    ' ': '0',
    '.': '1', ',': '11', '?': '111', '!': '1111', ':': '11111'
}


def text_messaging(message: str) -> str:
    pass


if __name__ == "__main__":
    print(text_messaging("HI"))  # "4444"
    print(text_messaging("HELLO"))  # "4433555555666"
    print(text_messaging("HI THERE"))  # "44440844433777733"
    print(text_messaging("HI!"))  # "4444441111"
    print(text_messaging("A"))  # "2"
    print(text_messaging(""))  # ""
```

## Hint

<details>
<summary>Click to reveal hint</summary>

Convert to uppercase, then iterate through each character and build the result:

```python
message = message.upper()
result = ""
for char in message:
    if char in T9_KEYPAD:
        result = result + T9_KEYPAD[char]
return result
```

Checking `if char in T9_KEYPAD` ensures that any character not in the keypad mapping is skipped.

</details>

## Note

<details>
<summary>Click to reveal note</summary>

**Historical Context:**

Before smartphones with touchscreens, text messaging on cellphones required pressing numeric keys multiple times to type each letter. This T9 (Text on 9 keys) system was the standard way to write messages.

For example, to type "HI":
- H: Press 4 twice (44)
- I: Press 4 three times (444)
- Result: "4444"

**Why This Encoding Matters:**

This exercise demonstrates:
1. **Dictionary mapping** - Each character maps to a specific key sequence
2. **Data transformation** - Converting from one format to another
3. **Historical technology** - Understanding constraints that shaped early mobile communication

Modern predictive text systems evolved from this, making texting much faster!

</details>

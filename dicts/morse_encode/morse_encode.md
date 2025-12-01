# Morse Code Encoder

Convert text to Morse code.

## Task

Write a function `morse_encode(text)` that converts a string to Morse code.

- Convert letters (A-Z) and digits (0-9) to their Morse code equivalents
- Use spaces to separate individual character codes
- Use ' / ' (space-slash-space) to represent word boundaries (spaces in the original text)
- The conversion should be case-insensitive (treat 'a' and 'A' the same)
- Skip characters that don't have a Morse code mapping
- Return empty string for empty input

## Template

```python
MORSE_CODE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    ' ': '/'
}


def morse_encode(text: str) -> str:
    pass


if __name__ == "__main__":
    print(morse_encode("SOS"))  # "... --- ..."
    print(morse_encode("HI THERE"))  # ".... .. / - .... . .-. ."
    print(morse_encode("123"))  # ".---- ..--- ...--"
    print(morse_encode("Hello"))  # ".... . .-.. .-.. ---"
    print(morse_encode(""))  # ""
    print(morse_encode("A"))  # ".-"
```

## Hint

<details>
<summary>Click to reveal hint</summary>

1. Convert the text to uppercase (since Morse code is case-insensitive)
2. Build a list of Morse codes for each character in the dictionary
3. Combine the results with spaces between them

```python
text = text.upper()
morse_chars = []
for char in text:
    if char in MORSE_CODE:
        morse_chars.append(MORSE_CODE[char])

result = ""
for i in range(len(morse_chars)):
    if i > 0:
        result = result + " "
    result = result + morse_chars[i]
return result
```

</details>

## Note

<details>
<summary>Click to reveal note</summary>

**Historical Context:**

Morse code was developed in the 1830s-1840s by Samuel Morse and Alfred Vail for use with the telegraph. It revolutionized long-distance communication by encoding text into sequences of dots (·) and dashes (—), which could be transmitted as electrical pulses.

The most famous Morse code sequence is "SOS" (... --- ...), which became the international distress signal because it's distinctive and easy to recognize.

**Encoding vs Encryption vs Hashing:**

This exercise demonstrates **encoding**, which is different from encryption and hashing:

- **Encoding** (like Morse code): Transforms data into another format using a known scheme. It's reversible and not secret. Anyone with the encoding scheme can decode it. Examples: Morse code, Base64, URL encoding.

- **Encryption**: Transforms data to keep it secret. Requires a key to decrypt. Examples: AES, RSA.

- **Hashing**: One-way transformation. Cannot be reversed to get original data. Examples: SHA-256, MD5 (for checksums/passwords).

</details>

# Morse Code Decoder

Convert Morse code back to text.

## Task

Write a function `morse_decode(morse)` that converts Morse code back to readable text.

- Individual character codes are separated by single spaces
- Word boundaries are represented by ' / ' (space-slash-space)
- Return the decoded text in uppercase
- Return empty string for empty input
- Handle invalid Morse code gracefully (skip unknown codes)

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

MORSE_TO_CHAR = {v: k for k, v in MORSE_CODE.items()}


def morse_decode(morse: str) -> str:
    pass


if __name__ == "__main__":
    print(morse_decode("... --- ..."))  # "SOS"
    print(morse_decode(".... .. / - .... . .-. . .-."))  # "HI THERE"
    print(morse_decode(".---- ..--- ...--"))  # "123"
    print(morse_decode(""))  # ""
    print(morse_decode(".-"))  # "A"
    print(morse_decode(".... . .-.. .-.. ---"))  # "HELLO"
```

## Hint

<details>
<summary>Click to reveal hint</summary>

1. Create a reverse dictionary that maps Morse code to characters
2. Split the input by ' / ' to separate words
3. For each word, split by ' ' to get individual letter codes
4. Look up each code in the reverse dictionary
5. Combine everything back together

```python
MORSE_TO_CHAR = {}
for k in MORSE_CODE:
    v = MORSE_CODE[k]
    MORSE_TO_CHAR[v] = k

words = morse.split(' / ')
decoded_words = []

for word in words:
    if word:
        letters = word.split(' ')
        decoded_word = ""
        for letter in letters:
            if letter in MORSE_TO_CHAR:
                decoded_word = decoded_word + MORSE_TO_CHAR[letter]
        decoded_words.append(decoded_word)

result = ""
for i in range(len(decoded_words)):
    if i > 0:
        result = result + " "
    result = result + decoded_words[i]
return result
```

</details>

## Note

<details>
<summary>Click to reveal note</summary>

**Reverse Dictionary Pattern:**

Creating a reverse mapping is a common pattern when you need bidirectional lookups:

```python
# Original mapping
MORSE_CODE = {'A': '.-', 'B': '-...', ...}

# Reverse mapping
MORSE_TO_CHAR = {}
for k in MORSE_CODE:
    v = MORSE_CODE[k]
    MORSE_TO_CHAR[v] = k
# {'.-': 'A', '-...': 'B', ...}
```

This technique works when the original dictionary has unique values. If values can repeat, the reverse dictionary will only keep the last key for each value.

**Why this approach?**

While we could search through MORSE_CODE for each Morse pattern, using a reverse dictionary gives us O(1) lookup instead of O(n) search, making decoding much faster for long messages.

</details>

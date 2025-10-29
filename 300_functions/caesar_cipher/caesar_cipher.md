# Caesar Cipher

Write a function that encrypts text using the Caesar cipher.

## Task
- Create a function `caesar_cipher(text, shift)` that takes text and shift amount
- Return the encrypted text

## Function Signature
```python
def caesar_cipher(text: str, shift: int) -> str:
    pass
```

## Examples
```python
caesar_cipher("abc", 1)        # "bcd"
caesar_cipher("xyz", 3)        # "abc"
caesar_cipher("Hello", 5)      # "Mjqqt"
caesar_cipher("ABC", -1)       # "ZAB"
```

## Logic
- Shift each letter by the specified amount
- Wrap around: 'z' + 1 = 'a', 'Z' + 1 = 'A'
- Preserve case (uppercase/lowercase)
- Leave non-letter characters unchanged

## Note
- Handle both positive and negative shifts
- Maintain the case of letters
- Don't modify spaces, punctuation, or numbers

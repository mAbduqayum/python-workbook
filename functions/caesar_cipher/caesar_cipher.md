# Caesar Cipher

Write a function that encrypts text using the Caesar cipher.

## Task
- Create a function `caesar_cipher(text, shift)` that takes text and shift amount
- Return the encrypted text
- Preserve letter case
- Leave non-letter characters (spaces, punctuation, digits) unchanged

## Template:
```python
def caesar_cipher(text: str, shift: int) -> str:
    pass


if __name__ == "__main__":
    # Test your function
    print(caesar_cipher("abc", 1))        # "bcd"
    print(caesar_cipher("xyz", 3))        # "abc"
    print(caesar_cipher("Hello", 5))      # "Mjqqt"
    print(caesar_cipher("ABC", -1))       # "ZAB"
```


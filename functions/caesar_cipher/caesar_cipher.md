# Caesar Cipher

Write a function that encrypts text using the Caesar cipher.

You wrote this as a program in [Caesar Cipher](../../repetitions/caesar_cipher/caesar_cipher.md); now make it a function.

## Task
- Create a function `caesar_cipher(text, shift)` that takes text and shift amount
- Return the encrypted text
- Preserve letter case
- Leave non-letter characters (spaces, punctuation, digits) unchanged

## Examples

| Call                                 | Returns           |
|--------------------------------------|-------------------|
| `caesar_cipher("xyz", 3)`            | `"abc"`           |
| `caesar_cipher("Hello, World!", 13)` | `"Uryyb, Jbeyq!"` |
| `caesar_cipher("ABC", -1)`           | `"ZAB"`           |


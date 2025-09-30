# Caesar Cipher

Implement a Caesar cipher to encode/decode messages by shifting letters.

## Task
- Read a message from the user
- Read a shift amount from the user
- Shift each letter by the specified amount
- Display the encoded/decoded message
- Support both uppercase and lowercase letters
- Support negative shift values (for decoding)
- Non-letter characters remain unchanged

## Examples
**Example 1:**
```
Enter message: HELLO
Enter shift: 3
```
```
KHOOR
```

**Example 2:**
```
Enter message: xyz
Enter shift: 3
```
```
abc
```

**Example 3:**
```
Enter message: Hello, World!
Enter shift: -3
```
```
Ebiil, Tloia!
```

## Logic
- For each character in the message:
  - If it's a letter:
    - Determine if uppercase or lowercase
    - Convert to position (A=0, B=1, ..., Z=25)
    - Add shift amount
    - Wrap around using modulo 26
    - Convert back to letter
  - If not a letter, keep as is

## Hints
- Use ord() to get ASCII value of character
- Use chr() to convert ASCII value to character
- ord('A') = 65, ord('a') = 97
- Use % 26 to wrap around the alphabet
- Check if character is letter with isalpha()

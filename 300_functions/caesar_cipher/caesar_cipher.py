def caesar_cipher(text: str, shift: int) -> str:
    result = ""
    
    for char in text:
        if char.isalpha():
            # Determine the base (A for uppercase, a for lowercase)
            base = ord('A') if char.isupper() else ord('a')
            # Shift the character and wrap around
            shifted = (ord(char) - base + shift) % 26
            result += chr(base + shifted)
        else:
            result += char
    
    return result


if __name__ == "__main__":
    # Test your function
    caesar_cipher("abc", 1)        # "bcd"
    caesar_cipher("xyz", 3)        # "abc"
    caesar_cipher("Hello", 5)      # "Mjqqt"
    caesar_cipher("ABC", -1)       # "ZAB"

def caesar_cipher(text: str, shift: int) -> str:
    """
    Encrypt text using the Caesar cipher.
    
    Args:
        text: The text to encrypt
        shift: The shift amount
        
    Returns:
        The encrypted text
    """
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

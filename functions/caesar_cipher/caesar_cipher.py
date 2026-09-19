def caesar_cipher(text: str, shift: int) -> str:
    result = ""

    for char in text:
        if char.isalpha():
            base = ord("A") if char.isupper() else ord("a")
            shifted = (ord(char) - base + shift) % 26
            result += chr(base + shifted)
        else:
            result += char

    return result


if __name__ == "__main__":
    print(caesar_cipher("abc", 1))  # "bcd"
    print(caesar_cipher("xyz", 3))  # "abc"
    print(caesar_cipher("Hello", 5))  # "Mjqqt"
    print(caesar_cipher("ABC", -1))  # "ZAB"

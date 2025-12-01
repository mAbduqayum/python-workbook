MORSE_CODE = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    " ": "/",
}


def morse_encode(text: str) -> str:
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


def morse_encode2(text: str) -> str:
    text = text.upper()
    morse_chars = [MORSE_CODE[char] for char in text if char in MORSE_CODE]
    return " ".join(morse_chars)


if __name__ == "__main__":
    print(morse_encode("SOS"))  # "... --- ..."
    print(morse_encode("HI THERE"))  # ".... .. / - .... . .-. ."
    print(morse_encode("123"))  # ".---- ..--- ...--"
    print(morse_encode("Hello"))  # ".... . .-.. .-.. ---"
    print(morse_encode(""))  # ""
    print(morse_encode("A"))  # ".-"

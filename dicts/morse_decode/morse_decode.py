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

MORSE_TO_CHAR = {}
for k in MORSE_CODE:
    v = MORSE_CODE[k]
    MORSE_TO_CHAR[v] = k


def morse_decode(morse: str) -> str:
    if not morse:
        return ""

    words = morse.split(" / ")
    decoded_words = []

    for word in words:
        if word:
            letters = word.split(" ")
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


def morse_decode2(morse: str) -> str:
    if not morse:
        return ""

    words = morse.split(" / ")
    decoded_words = []

    for word in words:
        if word:
            letters = word.split(" ")
            decoded_word = "".join(MORSE_TO_CHAR.get(letter, "") for letter in letters)
            decoded_words.append(decoded_word)

    return " ".join(decoded_words)


if __name__ == "__main__":
    print(morse_decode("... --- ..."))  # "SOS"
    print(morse_decode(".... .. / - .... . .-. . .-."))  # "HI THERE"
    print(morse_decode(".---- ..--- ...--"))  # "123"
    print(morse_decode(""))  # ""
    print(morse_decode(".-"))  # "A"
    print(morse_decode(".... . .-.. .-.. ---"))  # "HELLO"

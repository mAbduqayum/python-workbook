def tokenize(text: str) -> list[str]:
    # Keeps the characters between words too, so joining the tokens gives back text
    tokens = []
    start = 0
    for i, char in enumerate(text):
        if not char.isalnum():
            tokens.append(text[start:i])
            tokens.append(char)
            start = i + 1
    tokens.append(text[start:])
    return tokens


def redact_text(input_path: str, words_path: str, output_path: str) -> int:
    sensitive_words = set()
    with open(words_path, "r", encoding="utf-8") as f:
        for line in f:
            word = line.strip().lower()
            if word:
                sensitive_words.add(word)

    with open(input_path, "r", encoding="utf-8") as f:
        text = f.read()

    count = 0
    with open(output_path, "w", encoding="utf-8") as f:
        for token in tokenize(text):
            if token.lower() in sensitive_words:
                f.write("*" * len(token))
                count += 1
            else:
                f.write(token)

    return count


if __name__ == "__main__":
    with open("sensitive.txt", "w") as f:
        f.write("secret\npassword\nconfidential\n")

    with open("document.txt", "w") as f:
        f.write("This is a secret document.\n")
        f.write("The password is hidden.\n")
        f.write("Public information here.\n")

    print(redact_text("document.txt", "sensitive.txt", "redacted.txt"))  # 2

    with open("redacted.txt", "r") as f:
        print(f.read())

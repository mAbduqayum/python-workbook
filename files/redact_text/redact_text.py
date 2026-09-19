import re


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
    for word in sensitive_words:
        # \b word boundaries: match "secret" but not "secretly"
        pattern = re.compile(r"\b" + re.escape(word) + r"\b", re.IGNORECASE)
        matches = pattern.findall(text)
        count += len(matches)
        text = pattern.sub("*" * len(word), text)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)

    return count


if __name__ == "__main__":
    with open("sensitive.txt", "w") as f:
        f.write("secret\npassword\nconfidential\n")

    with open("document.txt", "w") as f:
        f.write("This is a secret document.\n")
        f.write("The password is hidden.\n")
        f.write("Public information here.\n")

    count = redact_text("document.txt", "sensitive.txt", "redacted.txt")
    print(f"Redacted {count} words")

    with open("redacted.txt", "r") as f:
        print(f.read())

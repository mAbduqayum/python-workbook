import re


def redact_text(input_path: str, words_path: str, output_path: str) -> int:
    # Load sensitive words
    sensitive_words = set()
    with open(words_path, "r", encoding="utf-8") as f:
        for line in f:
            word = line.strip().lower()
            if word:
                sensitive_words.add(word)

    # Read input text
    with open(input_path, "r", encoding="utf-8") as f:
        text = f.read()

    # Redact sensitive words
    count = 0
    for word in sensitive_words:
        # Create pattern that matches the word as a whole word
        pattern = re.compile(r"\b" + re.escape(word) + r"\b", re.IGNORECASE)
        matches = pattern.findall(text)
        count += len(matches)
        # Replace with asterisks of same length
        text = pattern.sub("*" * len(word), text)

    # Write output
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)

    return count


if __name__ == "__main__":
    # Create a sensitive words file
    with open("sensitive.txt", "w") as f:
        f.write("secret\npassword\nconfidential\n")

    # Create a text file
    with open("document.txt", "w") as f:
        f.write("This is a secret document.\n")
        f.write("The password is hidden.\n")
        f.write("Public information here.\n")

    # Test your function
    count = redact_text("document.txt", "sensitive.txt", "redacted.txt")
    print(f"Redacted {count} words")

    # View redacted file
    with open("redacted.txt", "r") as f:
        print(f.read())

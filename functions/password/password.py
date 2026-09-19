import random


def password(length: int) -> str:
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    special = "!@#$%^&*()"

    all_chars = lowercase + uppercase + digits + special

    # Guarantee at least one character from each category
    pwd = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special),
    ]

    for _ in range(length - len(pwd)):
        pwd.append(random.choice(all_chars))

    # Shuffle so the guaranteed characters don't always sit in the first four spots
    random.shuffle(pwd)

    return "".join(pwd)


if __name__ == "__main__":
    print(password(8))  # Random 8-character password
    print(password(12))  # Random 12-character password
    print(password(16))  # Random 16-character password

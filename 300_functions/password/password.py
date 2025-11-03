import random


def password(length: int) -> str:
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    special = "!@#$%^&*()"
    
    all_chars = lowercase + uppercase + digits + special
    
    # Ensure at least one character from each category
    pwd = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special),
    ]
    
    # Fill the rest randomly
    for _ in range(length - 4):
        pwd.append(random.choice(all_chars))
    
    # Shuffle to avoid predictable pattern
    random.shuffle(pwd)
    
    return ''.join(pwd)


if __name__ == "__main__":
    # Test your function
    password(8)      # Random 8-character password
    password(12)     # Random 12-character password
    password(16)     # Random 16-character password

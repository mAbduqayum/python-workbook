def decimal_hex(n: int) -> str:
    if n == 0:
        return "0"

    hex_digits = "0123456789ABCDEF"
    hex_str = ""

    while n > 0:
        hex_str = hex_digits[n % 16] + hex_str
        n //= 16

    return hex_str


if __name__ == "__main__":
    # Test your function
    print(decimal_hex(10))  # "A"
    print(decimal_hex(255))  # "FF"
    print(decimal_hex(16))  # "10"
    print(decimal_hex(26))  # "1A"
    print(decimal_hex(0))  # "0"

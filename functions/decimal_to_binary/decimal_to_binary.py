def decimal_to_binary(n: int) -> str:
    if n == 0:
        return "0"

    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n //= 2

    return binary


if __name__ == "__main__":
    # Test your function
    decimal_to_binary(10)  # "1010"
    decimal_to_binary(15)  # "1111"
    decimal_to_binary(0)  # "0"
    decimal_to_binary(1)  # "1"
    decimal_to_binary(16)  # "10000"

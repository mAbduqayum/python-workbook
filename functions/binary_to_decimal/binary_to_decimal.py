def binary_to_decimal(binary: str) -> int:
    decimal = 0
    power = 0

    for i in range(len(binary) - 1, -1, -1):
        if binary[i] == "1":
            decimal += 2**power
        power += 1

    return decimal


if __name__ == "__main__":
    # Test your function
    print(binary_to_decimal("1010"))  # 10
    print(binary_to_decimal("1111"))  # 15
    print(binary_to_decimal("0"))  # 0
    print(binary_to_decimal("1"))  # 1
    print(binary_to_decimal("10000"))  # 16

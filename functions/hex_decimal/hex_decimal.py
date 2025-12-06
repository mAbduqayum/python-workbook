def hex_decimal(hex_str: str) -> int:
    decimal = 0
    power = 0

    for i in range(len(hex_str) - 1, -1, -1):
        digit = hex_str[i].upper()
        if digit.isdigit():
            value = int(digit)
        else:
            value = ord(digit) - ord("A") + 10

        decimal += value * (16**power)
        power += 1

    return decimal


if __name__ == "__main__":
    # Test your function
    hex_decimal("A")  # 10
    hex_decimal("FF")  # 255
    hex_decimal("10")  # 16
    hex_decimal("1A")  # 26
    hex_decimal("ABC")  # 2748

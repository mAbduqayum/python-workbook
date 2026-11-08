def digits_only(number: str) -> str:
    return number.replace(" ", "")


def luhn_sum(digits: str) -> int:
    total = 0
    position = 1
    for i in range(len(digits) - 1, -1, -1):
        digit = int(digits[i])
        if position % 2 == 0:
            digit *= 2
            if digit > 9:
                digit -= 9
        total += digit
        position += 1
    return total


def is_valid_card(number: str) -> bool:
    return luhn_sum(digits_only(number)) % 10 == 0


if __name__ == "__main__":
    print(digits_only("4539 1488 0343 6467"))  # 4539148803436467
    print(luhn_sum("8763"))  # 20
    print(is_valid_card("79927398713"))  # True
    print(is_valid_card("79927398710"))  # False
    print(is_valid_card("4539 1488 0343 6467"))  # True

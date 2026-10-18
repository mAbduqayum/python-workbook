def list_total(numbers: list[int]) -> int:
    total = 0
    for number in numbers:
        total += number
    return total


if __name__ == "__main__":
    print(list_total([2, 3, 5, 7, 11]))  # 28
    print(list_total([]))  # 0

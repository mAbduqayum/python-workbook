def list_total(numbers: list[int]) -> int:
    total = 0
    for number in numbers:
        total += number
    return total


if __name__ == "__main__":
    # Test your function
    print(list_total([1, 2, 3, 4, 5]))  # 15
    print(list_total([10, -5, 3]))  # 8
    print(list_total([]))  # 0

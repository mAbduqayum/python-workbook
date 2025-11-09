def sort_numbers(numbers: list[int]) -> list[int]:
    return sorted(numbers)


if __name__ == "__main__":
    # Test your function
    print(sort_numbers([5, 2, 8, 1, 9]))  # [1, 2, 5, 8, 9]
    print(sort_numbers([3, 1, 2]))  # [1, 2, 3]

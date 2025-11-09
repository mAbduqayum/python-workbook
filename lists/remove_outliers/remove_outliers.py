def remove_outliers(numbers: list[int]) -> list[int]:
    result = numbers.copy()
    result.remove(min(numbers))
    result.remove(max(numbers))
    return result


if __name__ == "__main__":
    # Test your function
    print(remove_outliers([1, 2, 3, 4, 5]))  # [2, 3, 4]
    print(remove_outliers([10, 5, 8, 3]))  # [5, 8]

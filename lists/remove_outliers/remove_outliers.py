def remove_outliers(numbers: list[int]) -> list[int]:
    result = numbers.copy()
    result.remove(min(numbers))
    result.remove(max(numbers))
    return result


if __name__ == "__main__":
    print(remove_outliers([10, 5, 8, 3]))  # [5, 8]
    print(remove_outliers([1, 1, 5, 5]))  # [1, 5]

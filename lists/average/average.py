def average(numbers: list[int]) -> float:
    return sum(numbers) / len(numbers)


if __name__ == "__main__":
    # Test your function
    print(average([1, 2, 3, 4, 5]))  # 3.0
    print(average([10, 20, 30]))  # 20.0
    print(average([5]))  # 5.0

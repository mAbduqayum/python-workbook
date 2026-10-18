def average(numbers: list[int]) -> float:
    return sum(numbers) / len(numbers)


if __name__ == "__main__":
    print(average([2, 3, 5, 7, 11]))  # 5.6

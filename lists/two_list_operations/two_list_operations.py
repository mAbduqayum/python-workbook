def two_list_sum(list1: list[int], list2: list[int]) -> list[int]:
    return [a + b for a, b in zip(list1, list2)]


if __name__ == "__main__":
    # Test your function
    print(two_list_sum([1, 2, 3], [4, 5, 6]))  # [5, 7, 9]
    print(two_list_sum([10, 20], [5, 10]))  # [15, 30]

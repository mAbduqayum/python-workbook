def merge_and_sort(list1: list[int], list2: list[int]) -> list[int]:
    return sorted(list1 + list2)


if __name__ == "__main__":
    # Test your function
    print(merge_and_sort([1, 3, 5], [2, 4, 6]))  # [1, 2, 3, 4, 5, 6]
    print(merge_and_sort([1, 2], [3, 4]))  # [1, 2, 3, 4]

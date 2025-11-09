def slice_list(lst: list, start: int, end: int) -> list:
    return lst[start:end + 1]


if __name__ == "__main__":
    # Test your function
    print(slice_list([1, 2, 3, 4, 5], 1, 3))  # [2, 3, 4]
    print(slice_list(['a', 'b', 'c', 'd'], 0, 2))  # ['a', 'b', 'c']

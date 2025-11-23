def symmetric_diff(list1: list, list2: list) -> list:
    return list(set(list1) ^ set(list2))


if __name__ == "__main__":
    print(symmetric_diff([1, 2, 3], [2, 3, 4]))  # [1, 4] (order may vary)
    print(
        symmetric_diff(["a", "b", "c"], ["b", "c", "d"])
    )  # ['a', 'd'] (order may vary)
    print(symmetric_diff([1, 2], [1, 2]))  # []
    print(symmetric_diff([1, 2], [3, 4]))  # [1, 2, 3, 4] (order may vary)

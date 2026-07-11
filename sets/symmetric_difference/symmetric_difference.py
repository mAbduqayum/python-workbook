def symmetric_diff(list1: list, list2: list) -> list:
    return list(set(list1) ^ set(list2))


if __name__ == "__main__":
    print(symmetric_diff([2, 3, 5], [3, 5, 7]))  # [2, 7] (order may vary)
    print(
        symmetric_diff(["a", "b", "c"], ["b", "c", "d"])
    )  # ['a', 'd'] (order may vary)
    print(symmetric_diff([2, 3], [2, 3]))  # []
    print(symmetric_diff([2, 3], [5, 7]))  # [2, 3, 5, 7] (order may vary)

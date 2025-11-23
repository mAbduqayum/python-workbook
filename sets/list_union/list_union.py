def list_union(list1: list, list2: list) -> list:
    return list(set(list1) | set(list2))


if __name__ == "__main__":
    print(list_union([1, 2, 3], [3, 4, 5]))  # [1, 2, 3, 4, 5] (order may vary)
    print(
        list_union(["a", "b"], ["b", "c", "d"])
    )  # ['a', 'b', 'c', 'd'] (order may vary)
    print(list_union([], [1, 2]))  # [1, 2]
    print(list_union([1, 1, 2], [2, 2, 3]))  # [1, 2, 3] (order may vary)

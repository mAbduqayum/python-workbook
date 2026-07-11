def list_union(list1: list, list2: list) -> list:
    return list(set(list1) | set(list2))


if __name__ == "__main__":
    print(list_union([2, 3, 5], [5, 7, 11]))  # [2, 3, 5, 7, 11] (order may vary)
    print(
        list_union(["a", "b"], ["b", "c", "d"])
    )  # ['a', 'b', 'c', 'd'] (order may vary)
    print(list_union([], [2, 3]))  # [2, 3]
    print(list_union([2, 2, 3], [3, 3, 5]))  # [2, 3, 5] (order may vary)

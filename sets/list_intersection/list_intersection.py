def list_intersection(list1: list, list2: list) -> list:
    return list(set(list1) & set(list2))


if __name__ == "__main__":
    print(list_intersection([1, 2, 3, 4], [3, 4, 5, 6]))  # [3, 4] (order may vary)
    print(
        list_intersection(["a", "b", "c"], ["b", "c", "d"])
    )  # ['b', 'c'] (order may vary)
    print(list_intersection([1, 2], [3, 4]))  # []
    print(list_intersection([1, 1, 2, 2], [2, 2, 3, 3]))  # [2]

def list_intersection(list1: list, list2: list) -> list:
    return list(set(list1) & set(list2))


if __name__ == "__main__":
    print(list_intersection([2, 3, 5, 7], [5, 7, 11, 13]))  # [5, 7] (order may vary)
    print(
        list_intersection(["a", "b", "c"], ["b", "c", "d"])
    )  # ['b', 'c'] (order may vary)
    print(list_intersection([2, 3], [5, 7]))  # []
    print(list_intersection([2, 2, 3, 3], [3, 3, 5, 5]))  # [3]

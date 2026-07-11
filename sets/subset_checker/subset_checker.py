def is_subset(subset: list, superset: list) -> bool:
    return set(subset) <= set(superset)


if __name__ == "__main__":
    print(is_subset([2, 3], [2, 3, 5, 7]))  # True
    print(is_subset([2, 11], [2, 3, 5, 7]))  # False
    print(is_subset([], [2, 3, 5]))  # True
    print(is_subset([2, 3, 5], [2, 3, 5]))  # True
    print(is_subset(["a", "b"], ["a", "b", "c"]))  # True

def is_subset(subset: list, superset: list) -> bool:
    return set(subset) <= set(superset)


if __name__ == "__main__":
    print(is_subset([1, 2], [1, 2, 3, 4]))  # True
    print(is_subset([1, 5], [1, 2, 3, 4]))  # False
    print(is_subset([], [1, 2, 3]))  # True
    print(is_subset([1, 2, 3], [1, 2, 3]))  # True
    print(is_subset(["a", "b"], ["a", "b", "c"]))  # True

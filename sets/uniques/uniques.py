def uniques(values: list) -> list:
    return list(set(values))


if __name__ == "__main__":
    print(uniques([2, 3, 3, 5, 5, 5]))  # [2, 3, 5] (order may vary)
    print(uniques(["a", "b", "a", "c", "b"]))  # ['a', 'b', 'c'] (order may vary)
    print(uniques([]))  # []
    print(uniques([7, 7, 7, 7]))  # [7]

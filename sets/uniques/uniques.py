def uniques(values: list) -> list:
    return list(set(values))


if __name__ == "__main__":
    print(uniques([1, 2, 2, 3, 3, 3]))  # [1, 2, 3] (order may vary)
    print(uniques(["a", "b", "a", "c", "b"]))  # ['a', 'b', 'c'] (order may vary)
    print(uniques([]))  # []
    print(uniques([1, 1, 1, 1]))  # [1]

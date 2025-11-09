def copy_list(lst: list) -> list:
    return lst[:]


def are_different_objects(lst1: list, lst2: list) -> bool:
    return id(lst1) != id(lst2)


if __name__ == "__main__":
    # Test your functions
    original = [1, 2, 3, 4, 5]
    copied = copy_list(original)
    print(copied)  # [1, 2, 3, 4, 5]
    print(are_different_objects(original, copied))  # True

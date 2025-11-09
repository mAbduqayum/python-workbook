def is_sublist(main_list: list, sub: list) -> bool:
    if not sub:
        return True

    sub_len = len(sub)
    for i in range(len(main_list) - sub_len + 1):
        if main_list[i:i + sub_len] == sub:
            return True

    return False


if __name__ == "__main__":
    # Test your function
    print(is_sublist([1, 2, 3, 4, 5], [2, 3, 4]))  # True
    print(is_sublist([1, 2, 3, 4, 5], [2, 4]))  # False
    print(is_sublist([1, 2, 3], []))  # True

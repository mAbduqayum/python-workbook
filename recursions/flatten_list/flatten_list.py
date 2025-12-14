def flatten_list(lst: list) -> list:
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result


if __name__ == "__main__":
    print(flatten_list([1, 2, 3]))  # [1, 2, 3]
    print(flatten_list([1, [2, 3], 4]))  # [1, 2, 3, 4]
    print(flatten_list([[1, 2], [3, 4]]))  # [1, 2, 3, 4]
    print(flatten_list([1, [2, [3, [4]]]]))  # [1, 2, 3, 4]

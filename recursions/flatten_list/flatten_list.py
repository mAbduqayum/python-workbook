def flatten_list(l: list) -> list:
    result = []
    for item in l:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result


if __name__ == "__main__":
    print(flatten_list([2, 3, 5]))  # [2, 3, 5]
    print(flatten_list([2, [3, 5], 7]))  # [2, 3, 5, 7]
    print(flatten_list([[2, 3], [5, 7]]))  # [2, 3, 5, 7]
    print(flatten_list([2, [3, [5, [7]]]]))  # [2, 3, 5, 7]

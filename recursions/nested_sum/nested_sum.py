def nested_sum(l: list) -> int:
    total = 0
    for item in l:
        if isinstance(item, list):
            total += nested_sum(item)
        else:
            total += item
    return total


if __name__ == "__main__":
    print(nested_sum([2, 3, 5]))  # 10
    print(nested_sum([2, [3, 5], 7]))  # 17
    print(nested_sum([2, [3, [5, [7]]]]))  # 17
    print(nested_sum([[2, 3], [5, [7, 11]]]))  # 28

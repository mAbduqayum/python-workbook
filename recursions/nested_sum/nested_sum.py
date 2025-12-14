def nested_sum(lst: list) -> int:
    total = 0
    for item in lst:
        if isinstance(item, list):
            total += nested_sum(item)
        else:
            total += item
    return total


if __name__ == "__main__":
    print(nested_sum([1, 2, 3]))  # 6
    print(nested_sum([1, [2, 3], 4]))  # 10
    print(nested_sum([1, [2, [3, [4]]]]))  # 10
    print(nested_sum([[1, 2], [3, [4, 5]]]))  # 15

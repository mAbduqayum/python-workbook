def max_depth(data: list) -> int:
    deepest_child = 0
    for item in data:
        if isinstance(item, list):
            child_depth = max_depth(item)
            if child_depth > deepest_child:
                deepest_child = child_depth
    return deepest_child + 1


if __name__ == "__main__":
    print(max_depth([1, 2, 3]))  # 1
    print(max_depth([1, [2, 3]]))  # 2
    print(max_depth([1, [2, [3]], [4]]))  # 3
    print(max_depth([]))  # 1

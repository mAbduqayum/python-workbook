def sublists(lst: list) -> list[list]:
    result = [[]]  # Start with empty list
    for i in range(len(lst)):
        for j in range(i + 1, len(lst) + 1):
            result.append(lst[i:j])
    return result


if __name__ == "__main__":
    # Test your function
    print(sublists([1, 2, 3]))
    # [[], [1], [1, 2], [1, 2, 3], [2], [2, 3], [3]]

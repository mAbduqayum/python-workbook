def sublists(l: list) -> list[list]:
    result = [[]]  # Start with empty list
    for i in range(len(l)):
        for j in range(i + 1, len(l) + 1):
            result.append(l[i:j])
    return result


if __name__ == "__main__":
    # Test your function
    print(sublists([2, 3, 5]))
    # [[], [2], [2, 3], [2, 3, 5], [3], [3, 5], [5]]

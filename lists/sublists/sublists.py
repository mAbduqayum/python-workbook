def sublists(l: list) -> list[list]:
    result = [[]]  # the empty list is a sublist of every list
    for i in range(len(l)):
        for j in range(i + 1, len(l) + 1):
            result.append(l[i:j])
    return result


if __name__ == "__main__":
    print(sublists([2, 3, 5]))
    # [[], [2], [2, 3], [2, 3, 5], [3], [3, 5], [5]]

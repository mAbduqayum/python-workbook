def reverse_list(string: str) -> list[int]:
    if not string.strip():
        return []
    numbers = []
    for x in string.split():
        numbers.append(int(x))
    numbers.reverse()
    return numbers


def reverse_list2(string: str) -> list[int]:
    if not string.strip():
        return []
    numbers = [int(x) for x in string.split()]
    return numbers[::-1]


if __name__ == "__main__":
    # Test your function
    print(reverse_list("2 3 5 7 11"))  # [11, 7, 5, 3, 2]
    print(reverse_list("10 -5 3"))  # [3, -5, 10]
    print(reverse_list(""))  # []

def str_to_ints(string: str) -> list[int]:
    if not string.strip():
        return []
    result = []
    for x in string.split():
        result.append(int(x))
    return result


def str_to_ints2(string: str) -> list[int]:
    return [int(x) for x in string.split()]


if __name__ == "__main__":
    # Test your function
    print(str_to_ints("2 3 5 7 11"))  # [2, 3, 5, 7, 11]
    print(str_to_ints("10 -5 3"))  # [10, -5, 3]
    print(str_to_ints(""))  # []

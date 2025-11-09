def reverse_list(string: str) -> list[int]:
    if not string.strip():
        return []
    numbers = [int(x) for x in string.split()]
    return numbers[::-1]


if __name__ == "__main__":
    # Test your function
    print(reverse_list("1 2 3 4 5"))  # [5, 4, 3, 2, 1]
    print(reverse_list("10 -5 3"))  # [3, -5, 10]
    print(reverse_list(""))  # []

def to3x3matrix(string: str) -> list[list[int]]:
    numbers = []
    for x in string.split():
        numbers.append(int(x))
    result = []
    for i in range(0, 9, 3):
        row = []
        for j in range(3):
            row.append(numbers[i + j])
        result.append(row)
    return result


def to3x3matrix2(string: str) -> list[list[int]]:
    numbers = [int(x) for x in string.split()]
    return [numbers[i:i + 3] for i in range(0, 9, 3)]


if __name__ == "__main__":
    # Test your function
    matrix = to3x3matrix("1 2 3 4 5 6 7 8 9")
    for row in matrix:
        print(row)
    # Output:
    # [1, 2, 3]
    # [4, 5, 6]
    # [7, 8, 9]

def to_matrix(numbers: list[int], rows: int, cols: int) -> list[list[int]]:
    result = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(numbers[i * cols + j])
        result.append(row)
    return result


def to_matrix2(numbers: list[int], rows: int, cols: int) -> list[list[int]]:
    return [numbers[i * cols : (i + 1) * cols] for i in range(rows)]


if __name__ == "__main__":
    # Test your function
    print(to_matrix([2, 3, 5, 7, 11, 13], 2, 3))
    # [[2, 3, 5], [7, 11, 13]]

    print(to_matrix([2, 3, 5, 7], 2, 2))
    # [[2, 3], [5, 7]]

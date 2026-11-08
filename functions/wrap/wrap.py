def wrap(value: int, low: int, high: int) -> int:
    size = high - low + 1
    return low + (value - low) % size


if __name__ == "__main__":
    print(wrap(13, 1, 12))  # 1
    print(wrap(0, 1, 12))  # 12
    print(wrap(25, 1, 12))  # 1
    print(wrap(7, 1, 12))  # 7
    print(wrap(10, 0, 6))  # 3
    print(wrap(-1, 0, 6))  # 6

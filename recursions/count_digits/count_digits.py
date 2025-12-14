def count_digits(n: int) -> int:
    n = abs(n)
    if n < 10:
        return 1
    return 1 + count_digits(n // 10)


if __name__ == "__main__":
    print(count_digits(0))  # 1
    print(count_digits(5))  # 1
    print(count_digits(123))  # 3
    print(count_digits(1000000))  # 7

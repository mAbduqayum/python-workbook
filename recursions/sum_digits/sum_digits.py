def sum_digits(n: int) -> int:
    n = abs(n)
    if n < 10:
        return n
    return (n % 10) + sum_digits(n // 10)


if __name__ == "__main__":
    print(sum_digits(0))  # 0
    print(sum_digits(123))  # 6
    print(sum_digits(9999))  # 36
    print(sum_digits(-456))  # 15

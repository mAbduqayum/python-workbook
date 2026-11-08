def sum_digits(n: int) -> int:
    if n < 10:
        return n
    return n % 10 + sum_digits(n // 10)


def digital_root(n: int) -> int:
    if n < 10:
        return n
    return digital_root(sum_digits(n))


if __name__ == "__main__":
    print(digital_root(9875))  # 2
    print(digital_root(38))  # 2
    print(digital_root(7))  # 7

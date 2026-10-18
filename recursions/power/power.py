def power(base: int, exp: int) -> int:
    if exp == 0:
        return 1
    return base * power(base, exp - 1)


if __name__ == "__main__":
    print(power(2, 0))  # 1
    print(power(2, 3))  # 8

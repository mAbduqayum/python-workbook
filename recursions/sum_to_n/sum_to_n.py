def sum_to_n(n: int) -> int:
    if n == 1:
        return 1
    return n + sum_to_n(n - 1)


if __name__ == "__main__":
    print(sum_to_n(1))  # 1
    print(sum_to_n(5))  # 15
    print(sum_to_n(10))  # 55
    print(sum_to_n(100))  # 5050

def factorial(n: int) -> int:
    if n <= 1:
        return 1
    return n * factorial(n - 1)


if __name__ == "__main__":
    print(factorial(0))  # 1
    print(factorial(1))  # 1
    print(factorial(5))  # 120
    print(factorial(10))  # 3628800

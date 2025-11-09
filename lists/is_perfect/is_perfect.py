from lists.divisors.divisors import divisors


def is_perfect(n: int) -> bool:
    return sum(divisors(n)) - n == n


if __name__ == "__main__":
    # Test your function
    print(is_perfect(6))  # True (1 + 2 + 3 = 6)
    print(is_perfect(28))  # True (1 + 2 + 4 + 7 + 14 = 28)
    print(is_perfect(12))  # False

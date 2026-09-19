def gcd(a: int, b: int) -> int:
    # Euclidean algorithm
    while b != 0:
        a, b = b, a % b
    return a


def normalize_fraction(numerator: int, denominator: int) -> tuple[int, int]:
    if numerator == 0:
        return 0, 1

    divisor = gcd(abs(numerator), abs(denominator))
    return numerator // divisor, denominator // divisor


if __name__ == "__main__":
    print(normalize_fraction(4, 8))  # (1, 2)
    print(normalize_fraction(6, 9))  # (2, 3)
    print(normalize_fraction(5, 10))  # (1, 2)
    print(normalize_fraction(7, 3))  # (7, 3)
    print(normalize_fraction(0, 5))  # (0, 1)

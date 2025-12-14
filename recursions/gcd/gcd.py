def gcd(a: int, b: int) -> int:
    if b == 0:
        return a
    return gcd(b, a % b)


if __name__ == "__main__":
    print(gcd(48, 18))  # 6
    print(gcd(18, 48))  # 6
    print(gcd(100, 25))  # 25
    print(gcd(17, 13))  # 1

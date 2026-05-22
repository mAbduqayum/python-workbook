def is_even(n: int) -> bool:
    return n % 2 == 0


if __name__ == "__main__":
    # Test your function
    print(is_even(4))  # True
    print(is_even(7))  # False
    print(is_even(0))  # True
    print(is_even(-2))  # True
    print(is_even(-5))  # False

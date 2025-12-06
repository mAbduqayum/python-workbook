def is_even(n: int) -> bool:
    return n % 2 == 0


if __name__ == "__main__":
    # Test your function
    is_even(4)  # True
    is_even(7)  # False
    is_even(0)  # True
    is_even(-2)  # True
    is_even(-5)  # False

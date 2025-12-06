def is_leap_year(year: int) -> bool:
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False


if __name__ == "__main__":
    # Test your function
    is_leap_year(2000)  # True
    is_leap_year(2004)  # True
    is_leap_year(1900)  # False
    is_leap_year(2001)  # False
    is_leap_year(2024)  # True

def days_in_month(year: int, month: int) -> int:
    if month == 2:
        if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
            return 29
        return 28
    if month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    return 31


def ordinal_to_gregorian(year: int, day_of_year: int) -> tuple[int, int, int]:
    for month in range(1, 13):
        days = days_in_month(year, month)
        if day_of_year <= days:
            return year, month, day_of_year
        day_of_year -= days

    # Should not reach here with valid input
    return year, 12, 31


if __name__ == "__main__":
    print(ordinal_to_gregorian(2024, 1))  # (2024, 1, 1)
    print(ordinal_to_gregorian(2024, 32))  # (2024, 2, 1)
    print(ordinal_to_gregorian(2024, 60))  # (2024, 2, 29)
    print(ordinal_to_gregorian(2023, 60))  # (2023, 3, 1)
    print(ordinal_to_gregorian(2024, 366))  # (2024, 12, 31)

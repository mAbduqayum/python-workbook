def ordinal_to_gregorian(year: int, day_of_year: int) -> tuple[int, int, int]:
    # Check if leap year
    is_leap = (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

    # Days in each month
    days_in_month = [31, 29 if is_leap else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    month = 1
    for days in days_in_month:
        if day_of_year <= days:
            return year, month, day_of_year
        day_of_year -= days
        month += 1

    # Should not reach here with valid input
    return year, 12, 31


if __name__ == "__main__":
    # Test your function
    ordinal_to_gregorian(2024, 1)  # (2024, 1, 1)
    ordinal_to_gregorian(2024, 32)  # (2024, 2, 1)
    ordinal_to_gregorian(2024, 60)  # (2024, 2, 29)
    ordinal_to_gregorian(2023, 60)  # (2023, 3, 1)
    ordinal_to_gregorian(2024, 366)  # (2024, 12, 31)

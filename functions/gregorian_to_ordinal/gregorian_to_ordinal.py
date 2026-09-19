def gregorian_to_ordinal(year: int, month: int, day: int) -> int:
    is_leap = (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)
    days_in_month = [31, 29 if is_leap else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    days_in_previous_months = sum(days_in_month[: month - 1])
    return days_in_previous_months + day


if __name__ == "__main__":
    print(gregorian_to_ordinal(2024, 1, 1))  # 1
    print(gregorian_to_ordinal(2024, 2, 1))  # 32
    print(gregorian_to_ordinal(2024, 2, 29))  # 60
    print(gregorian_to_ordinal(2023, 3, 1))  # 60
    print(gregorian_to_ordinal(2024, 12, 31))  # 366

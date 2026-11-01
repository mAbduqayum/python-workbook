def days_in_month(year: int, month: int) -> int:
    if month == 2:
        if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
            return 29
        return 28
    if month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    return 31


def gregorian_to_ordinal(year: int, month: int, day: int) -> int:
    day_of_year = day
    for earlier_month in range(1, month):
        day_of_year += days_in_month(year, earlier_month)
    return day_of_year


if __name__ == "__main__":
    print(gregorian_to_ordinal(2024, 1, 1))  # 1
    print(gregorian_to_ordinal(2024, 2, 1))  # 32
    print(gregorian_to_ordinal(2024, 2, 29))  # 60
    print(gregorian_to_ordinal(2023, 3, 1))  # 60
    print(gregorian_to_ordinal(2024, 12, 31))  # 366

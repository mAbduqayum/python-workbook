def is_leap_year(year: int) -> bool:
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False


def days_in_month(year: int, month: int) -> int:
    match month:
        case 2:
            if is_leap_year(year):
                return 29
            return 28
        case 4 | 6 | 9 | 11:
            return 30
        case _:
            return 31


def is_valid_date(year: int, month: int, day: int) -> bool:
    if month < 1 or month > 12:
        return False
    return 1 <= day <= days_in_month(year, month)


if __name__ == "__main__":
    print(days_in_month(2023, 4))  # 30
    print(days_in_month(2024, 2))  # 29
    print(is_valid_date(2024, 2, 29))  # True
    print(is_valid_date(2023, 2, 29))  # False
    print(is_valid_date(2023, 4, 31))  # False
    print(is_valid_date(2023, 13, 1))  # False

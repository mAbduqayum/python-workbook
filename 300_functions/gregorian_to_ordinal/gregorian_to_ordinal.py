def gregorian_to_ordinal(year: int, month: int, day: int) -> int:
    # Check if leap year
    is_leap = (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)
    
    # Days in each month
    days_in_month = [31, 29 if is_leap else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # Sum days from previous months
    day_of_year = sum(days_in_month[:month - 1]) + day
    
    return day_of_year


if __name__ == "__main__":
    # Test your function
    gregorian_to_ordinal(2024, 1, 1)      # 1
    gregorian_to_ordinal(2024, 2, 1)      # 32
    gregorian_to_ordinal(2024, 2, 29)     # 60
    gregorian_to_ordinal(2023, 3, 1)      # 60
    gregorian_to_ordinal(2024, 12, 31)    # 366

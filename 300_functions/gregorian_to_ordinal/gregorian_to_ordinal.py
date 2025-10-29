def gregorian_to_ordinal(year: int, month: int, day: int) -> int:
    """
    Convert a Gregorian date to ordinal date (day of year).
    
    Args:
        year: The year
        month: The month (1-12)
        day: The day of month
        
    Returns:
        Day of the year (1-366)
    """
    # Check if leap year
    is_leap = (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)
    
    # Days in each month
    days_in_month = [31, 29 if is_leap else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # Sum days from previous months
    day_of_year = sum(days_in_month[:month - 1]) + day
    
    return day_of_year

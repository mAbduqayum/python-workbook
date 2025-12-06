year = int(input())
month = int(input())
day = int(input())

days_in_month = 31
match month:
    case 2:
        days_in_month = 28
        is_leap = year % 400 == 0 or year % 4 == 0 and year % 100 != 0
        if is_leap:
            days_in_month += 1
    case 4 | 6 | 9 | 11:
        days_in_month = 30

next_day = day + 1
next_month = month
next_year = year

if next_day > days_in_month:
    next_day = 1
    next_month += 1
    if next_month > 12:
        next_month = 1
        next_year += 1

print(f"{next_year}-{next_month:02d}-{next_day:02d}")

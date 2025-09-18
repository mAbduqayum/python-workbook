year = int(input())
month = int(input())
day = int(input())

is_leap = year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

if month == 2:
    days_in_month = 29 if is_leap else 28
elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    days_in_month = 31
else:
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

month_str = f"{next_month:02d}"
day_str = f"{next_day:02d}"

print(f"{next_year}-{month_str}-{day_str}")
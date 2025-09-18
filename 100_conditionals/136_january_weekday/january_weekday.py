year = int(input())

# Calculate day of week for January 1st
day_of_week = (year + (year - 1) // 4 - (year - 1) // 100 + (year - 1) // 400) % 7

weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
print(weekdays[day_of_week])
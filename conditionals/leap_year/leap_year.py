year = int(input())

# `and` binds tighter than `or`: divisible by 400, or (by 4 and not by 100)
if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
    print("Leap year")
else:
    print("Not leap year")

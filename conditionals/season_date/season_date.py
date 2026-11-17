month = input().lower()
day = int(input())

if month == "january" or month == "february":
    print("winter")
elif month == "march":
    if day < 20:
        print("winter")
    else:
        print("spring")
elif month == "april" or month == "may":
    print("spring")
elif month == "june":
    if day < 21:
        print("spring")
    else:
        print("summer")
elif month == "july" or month == "august":
    print("summer")
elif month == "september":
    if day < 22:
        print("summer")
    else:
        print("fall")
elif month == "october" or month == "november":
    print("fall")
elif month == "december":
    if day < 21:
        print("fall")
    else:
        print("winter")

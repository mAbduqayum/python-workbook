month = input().lower()
day = int(input())

if month == "january" or month == "february":
    print("Winter")
elif month == "march":
    if day < 20:
        print("Winter")
    else:
        print("Spring")
elif month == "april" or month == "may":
    print("Spring")
elif month == "june":
    if day < 21:
        print("Spring")
    else:
        print("Summer")
elif month == "july" or month == "august":
    print("Summer")
elif month == "september":
    if day < 22:
        print("Summer")
    else:
        print("Fall")
elif month == "october" or month == "november":
    print("Fall")
elif month == "december":
    if day < 21:
        print("Fall")
    else:
        print("Winter")

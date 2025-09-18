month = input().lower()

if month == "february":
    print("28 or 29")
elif month in ["january", "march", "may", "july", "august", "october", "december"]:
    print("31")
elif month in ["april", "june", "september", "november"]:
    print("30")
else:
    print("Invalid month")
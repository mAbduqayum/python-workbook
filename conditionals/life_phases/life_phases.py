age = int(input())

if age < 0:
    print("invalid age")
elif age < 2:
    print("infant")
elif age < 5:
    print("toddler")
elif age < 11:
    print("child")
elif age < 18:
    print("adolescent")
elif age < 40:
    print("young adult")
elif age < 65:
    print("middle-aged")
else:
    print("senior")

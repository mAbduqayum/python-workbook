age = int(input())

if age < 0:
    print("Invalid age")
elif age <= 2:
    print("Infant")
elif age <= 5:
    print("Toddler")
elif age <= 11:
    print("Child")
elif age <= 18:
    print("Adolescent")
elif age <= 40:
    print("Young Adult")
elif age <= 65:
    print("Middle-aged")
else:
    print("Senior")
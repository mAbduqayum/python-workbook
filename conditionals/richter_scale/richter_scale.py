magnitude = float(input())

if magnitude < 2.0:
    print("Micro")
elif magnitude < 3.0:
    print("Very Minor")
elif magnitude < 4.0:
    print("Minor")
elif magnitude < 5.0:
    print("Light")
elif magnitude < 6.0:
    print("Moderate")
elif magnitude < 7.0:
    print("Strong")
elif magnitude < 8.0:
    print("Major")
elif magnitude < 10.0:
    print("Great")
else:
    print("Meteoric")

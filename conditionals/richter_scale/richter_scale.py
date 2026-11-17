magnitude = float(input())

if magnitude < 2.0:
    print("micro")
elif magnitude < 3.0:
    print("very minor")
elif magnitude < 4.0:
    print("minor")
elif magnitude < 5.0:
    print("light")
elif magnitude < 6.0:
    print("moderate")
elif magnitude < 7.0:
    print("strong")
elif magnitude < 8.0:
    print("major")
elif magnitude < 10.0:
    print("great")
else:
    print("meteoric")

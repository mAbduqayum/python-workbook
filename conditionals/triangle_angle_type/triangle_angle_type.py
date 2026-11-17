angle1 = float(input())
angle2 = float(input())
angle3 = float(input())

if angle1 + angle2 + angle3 != 180:
    print("invalid triangle")
elif angle1 == 90 or angle2 == 90 or angle3 == 90:
    print("right triangle")
elif angle1 > 90 or angle2 > 90 or angle3 > 90:
    print("obtuse triangle")
else:
    print("acute triangle")

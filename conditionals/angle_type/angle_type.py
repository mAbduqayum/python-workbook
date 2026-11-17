angle = int(input())

if angle <= 0 or angle > 360:
    print("invalid angle")
elif angle < 90:
    print("acute angle")
elif angle == 90:
    print("right angle")
elif angle < 180:
    print("obtuse angle")
elif angle == 180:
    print("straight angle")
elif angle < 360:
    print("reflex angle")
else:  # angle == 360
    print("full rotation")

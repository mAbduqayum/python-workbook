angle = int(input())

# Python's % is never negative, so this lands in [0, 360) even for negative angles
angle = angle % 360

if angle == 0 or angle == 90 or angle == 180 or angle == 270:
    print("On axis")
elif 0 < angle < 90:
    print("Quadrant I")
elif 90 < angle < 180:
    print("Quadrant II")
elif 180 < angle < 270:
    print("Quadrant III")
else:  # 270 < angle < 360
    print("Quadrant IV")

angle1 = float(input())
angle2 = float(input())
angle3 = float(input())

# Check if angles form a valid triangle
if angle1 + angle2 + angle3 != 180:
    print("Invalid Triangle")
elif angle1 == 90 or angle2 == 90 or angle3 == 90:
    print("Right Triangle")
elif angle1 > 90 or angle2 > 90 or angle3 > 90:
    print("Obtuse Triangle")
else:
    print("Acute Triangle")
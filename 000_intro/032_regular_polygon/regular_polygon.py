import math

n = int(input("Enter number of sides: "))
s = float(input("Enter side length: "))
area = (n * s * s) / (4 * math.tan(math.pi / n))
print(f"Area of regular polygon: {area:.2f}")

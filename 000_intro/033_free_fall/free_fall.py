import math

height = float(input("Enter height (meters): "))
velocity = math.sqrt(2 * 9.8 * height)
print(f"Final velocity: {velocity:.2f} m/s")

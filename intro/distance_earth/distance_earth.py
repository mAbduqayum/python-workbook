import math

lat1 = math.radians(float(input("Enter first latitude: ")))
lon1 = math.radians(float(input("Enter first longitude: ")))
lat2 = math.radians(float(input("Enter second latitude: ")))
lon2 = math.radians(float(input("Enter second longitude: ")))
distance = 6371.01 * math.acos(
    math.sin(lat1) * math.sin(lat2)
    + math.cos(lat1) * math.cos(lat2) * math.cos(lon1 - lon2)
)
print(f"Distance: {distance:.2f} km")

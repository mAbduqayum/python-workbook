volume = float(input("Enter volume of water (liters): "))
temp_change = float(input("Enter temperature change (°C): "))
mass = volume * 1000
energy = mass * 4.186 * temp_change / 3600000
cost = energy * 0.04
print(f"Energy required: {energy:.2f} kWh")
print(f"Cost to heat water: ${cost:.2f}")

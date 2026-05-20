mass = float(input("Enter mass of water (grams): "))
temp_change = float(input("Enter temperature change (°C): "))
energy = mass * 4.186 * temp_change
cost = energy / 3600000 * 0.40
print(f"Energy required: {energy:.2f} Joules")
print(f"Cost to heat water: {cost:.2f} somoni")

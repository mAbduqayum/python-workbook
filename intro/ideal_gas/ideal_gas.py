pressure = float(input("Enter pressure (Pascals): "))
volume_liters = float(input("Enter volume (liters): "))
temp_celsius = float(input("Enter temperature (°C): "))
temp_kelvin = temp_celsius + 273.15
volume = volume_liters / 1000  # cubic
n = (pressure * volume) / (8.314 * temp_kelvin)
print(f"Amount of gas: {n:.2f} moles")

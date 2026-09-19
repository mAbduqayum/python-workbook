pressure = float(input("Enter pressure (Pascals): "))
volume_liters = float(input("Enter volume (liters): "))
temp_celsius = float(input("Enter temperature (°C): "))
temp_kelvin = temp_celsius + 273.15
volume_m3 = volume_liters / 1000

gas_constant = 8.314  # J/(mol·K)
n = (pressure * volume_m3) / (gas_constant * temp_kelvin)
print(f"Amount of gas: {n:.2f} moles")

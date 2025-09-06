# Exercise: Ideal Gas Law

Write a program that calculates the amount of gas in moles using the ideal gas law.

## Task
- Read pressure in Pascals (as `float`)
- Read volume in liters (as `float`)
- Read temperature in degrees Celsius (as `float`)
- Calculate and display the amount of gas in moles

## Examples
**Example 1:**
```
Enter pressure (Pascals): 20000000
Enter volume (liters): 12
Enter temperature (°C): 20
Amount of gas: 98.47 moles
```

**Example 2:**
```
Enter pressure (Pascals): 101325
Enter volume (liters): 22.4
Temperature (°C): 0
Amount of gas: 1.00 moles
```

**Example 3:**
```
Enter pressure (Pascals): 500000
Enter volume (liters): 5
Enter temperature (°C): 25
Amount of gas: 1.01 moles
```

## Formula
`PV = nRT` → `n = PV / (RT)` where:
- `P` = pressure in Pascals
- `V` = volume in liters  
- `n` = amount in moles
- `R = 8.314 J/(mol·K)` (ideal gas constant)
- `T` = temperature in Kelvin = `°C + 273.15`

## Note
- Use `.2f` formatting to display 2 decimal places
- Convert Celsius to Kelvin: `K = °C + 273.15`
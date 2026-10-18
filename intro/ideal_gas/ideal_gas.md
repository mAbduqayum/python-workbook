# Exercise: Ideal Gas Law

Write a program that calculates the amount of gas in moles using the ideal gas law.

## Examples

**Example 1:**

```
Enter pressure (Pascals): 20000000
Enter volume (liters): 12
Enter temperature (°C): 20
```

```
Amount of gas: 98.47 moles
```

## Formula

`PV = nRT` → `n = PV / (RT)` where:

- `P` = pressure in Pascals
- `V` = volume in cubic meters (convert from liters: `1 liter = 0.001 m³`)
- `n` = amount in moles
- `R = 8.314 J/(mol·K)` (ideal gas constant)
- `T` = temperature in Kelvin = `°C + 273.15`

# Exercise: Heat Capacity

Write a program that calculates the energy (kWh) required to heat water and the cost in dollars (electricity costs `$0.04/kWh` in Tajikistan).

## Examples

**Example 1:**

```
Enter volume of water (liters): 2
Enter temperature change (°C): 90
```

```
Energy required: 0.21 kWh
Cost to heat water: $0.01
```

## Formula

- Energy: `q = m × C × 𝚫T` where `C = 4.186 J/(g·°C)`
- Convert to kWh: 1 kWh = 3,600,000 J
- Cost: `cost = kWh × 0.04`

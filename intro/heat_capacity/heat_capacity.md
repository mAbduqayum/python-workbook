# Exercise: Heat Capacity

Write a program that calculates the energy (Joules) required to heat water and the cost in somoni (electricity costs `0.40 somoni/kWh` in Tajikistan).

## Examples

**Example 1:**

```
Enter mass of water (grams): 250
Enter temperature change (°C): 75
```

```
Energy required: 78487.50 Joules
Cost to heat water: 0.01 somoni
```

**Example 2:**

```
Enter mass of water (grams): 1000
Enter temperature change (°C): 80
```

```
Energy required: 334880.00 Joules
Cost to heat water: 0.04 somoni
```

**Example 3:**

```
Enter mass of water (grams): 500
Enter temperature change (°C): 95
```

```
Energy required: 198835.00 Joules
Cost to heat water: 0.02 somoni
```

## Formula

- Energy: `q = m × C × 𝚫T` where `C = 4.186 J/(g·°C)`
- Cost: `cost = energy_in_joules / 3600000 × 0.40`


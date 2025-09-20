# Exercise: Heat Capacity

Write a program that calculates the energy required to heat water and the cost of heating.

## Task

- Read the mass of water in grams (as `float`)
- Read the temperature change in degrees Celsius (as `float`)
- Calculate energy required in Joules
- Calculate cost in euros (assuming electricity costs 0.089 euros per kWh)

## Examples

**Example 1:**

```
Enter mass of water (grams): 250
Enter temperature change (°C): 75
```

```
Energy required: 78487.50 Joules
Cost to heat water: 0.00 euros
```

**Example 2:**

```
Enter mass of water (grams): 1000
Enter temperature change (°C): 80
```

```
Energy required: 334880.00 Joules
Cost to heat water: 0.01 euros
```

**Example 3:**

```
Enter mass of water (grams): 500
Enter temperature change (°C): 95
```

```
Energy required: 198835.00 Joules
Cost to heat water: 0.00 euros
```

## Formula

- Energy: `q = m × C × 𝚫T` where `C = 4.186 J/(g·°C)`
- Cost: `cost = energy_in_joules / 3600000 × 0.089`

## Note

- Use `.2f` formatting to display 2 decimal places
- Water's specific heat capacity is `4.186 J/(g·°C)`
- `1 kWh = 3,600,000 Joules`

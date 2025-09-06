# Exercise: Units of Pressure

Write a program that converts pressure from kilopascals to other metric units.

## Task
- Read pressure in kilopascals (as `float`)
- Convert and display in pascals, bars, and atmospheres

## Examples
**Example 1:**
```
Enter pressure in kilopascals: 101.325
Pressure in pascals: 101325.00
Pressure in bars: 1.01
Pressure in atmospheres: 1.00
```

**Example 2:**
```
Enter pressure in kilopascals: 200
Pressure in pascals: 200000.00
Pressure in bars: 2.00
Pressure in atmospheres: 1.97
```

**Example 3:**
```
Enter pressure in kilopascals: 50
Pressure in pascals: 50000.00
Pressure in bars: 0.50
Pressure in atmospheres: 0.49
```

## Formula
- Pascals: `Pa = kPa × 1000`
- Bars: `bar = kPa / 100`
- Atmospheres: `atm = kPa / 101.325`

## Note
Use `.2f` formatting to display 2 decimal places.
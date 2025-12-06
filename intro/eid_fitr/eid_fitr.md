# Skip this question

---

# Exercise: When is Eid al-Fitr

Write a program that estimates Eid al-Fitr date (simplified lunar calendar calculation).

## Task

- Read a Gregorian year (as `int`)
- Calculate and display the estimated date for Eid al-Fitr in that year
- Note: This is a simplified approximation

## Examples

**Example 1:**

```
Enter Gregorian year: 2024
```

```
Estimated Eid al-Fitr: 2024/04/10
```

**Example 2:**

```
Enter Gregorian year: 2025
```

```
Estimated Eid al-Fitr: 2025/03/30
```

**Example 3:**

```
Enter Gregorian year: 2026
```

```
Estimated Eid al-Fitr: 2026/03/20
```

## Formula (Simplified)

- Convert Gregorian year to approximate Hijri year: `hijri_year ≈ (gregorian_year - 622) × 1.030684`
- Calculate Eid al-Fitr date using lunar calendar approximation
- Eid al-Fitr is on the 1st of Shawwal (10th month)

## Note

- This is a simplified calculation for educational purposes
- Real Hijri calendar calculations are more complex
- Actual dates may vary by 1-2 days due to moon sighting

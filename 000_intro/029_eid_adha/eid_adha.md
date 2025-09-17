# Skip this question

---

# Exercise: When is Eid al-Adha

Write a program that estimates Eid al-Adha date (simplified lunar calendar calculation).

## Task
- Read a Gregorian year (as `int`)
- Calculate and display the estimated date for Eid al-Adha in that year
- Note: This is a simplified approximation

## Examples
**Example 1:**
```
Enter Gregorian year: 2024
```
```
Estimated Eid al-Adha: June 16, 2024
```

**Example 2:**
```
Enter Gregorian year: 2025
```
```
Estimated Eid al-Adha: June 6, 2025
```

**Example 3:**
```
Enter Gregorian year: 2026
```
```
Estimated Eid al-Adha: May 26, 2026
```

## Formula (Simplified)
- Convert Gregorian year to approximate Hijri year: `hijri_year ≈ (gregorian_year - 622) × 1.030684`
- Calculate Eid al-Adha date using lunar calendar approximation
- Eid al-Adha is on the 10th of Dhul Hijjah (12th month)

## Note
- This is a simplified calculation for educational purposes
- Real Hijri calendar calculations are more complex
- Actual dates may vary by 1-2 days due to moon sighting
- Eid al-Adha occurs ~70 days after Eid al-Fitr

# Roman Numeral to Integer

Convert a Roman numeral string to an integer.

## Task

Write a function `roman_to_int(roman)` that converts a Roman numeral string to its integer value.

- Support the standard Roman numeral symbols: I (1), V (5), X (10), L (50), C (100), D (500), M (1000)
- Handle subtraction cases: IV (4), IX (9), XL (40), XC (90), CD (400), CM (900)
- Input will be a valid Roman numeral string
- Roman numerals are written from largest to smallest, left to right, except for subtraction cases

## Template

```python
ROMAN = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}


def roman_to_int(roman: str) -> int:
    pass


if __name__ == "__main__":
    print(roman_to_int("III"))  # 3
    print(roman_to_int("IV"))  # 4
    print(roman_to_int("IX"))  # 9
    print(roman_to_int("LVIII"))  # 58
    print(roman_to_int("MCMXCIV"))  # 1994
    print(roman_to_int("I"))  # 1
    print(roman_to_int("XIV"))  # 14
```

## Hint

<details>
<summary>Click to reveal hint</summary>

The key insight: when a smaller numeral appears before a larger one, subtract it; otherwise, add it.

```python
total = 0
for i in range(len(roman)):
    current = ROMAN[roman[i]]
    # Check if next numeral is larger
    if i + 1 < len(roman) and current < ROMAN[roman[i + 1]]:
        total -= current  # Subtraction case (like IV, IX)
    else:
        total += current  # Normal case
return total
```

Examples:
- "IV": I (1) < V (5), so subtract: -1 + 5 = 4
- "VI": V (5) > I (1), so add: 5 + 1 = 6
- "MCMXCIV": M(1000) + CM(900) + XC(90) + IV(4) = 1994

</details>

## Note

<details>
<summary>Click to reveal note</summary>

**Roman Numeral Rules:**

Roman numerals use a subtractive notation for specific cases to avoid writing four of the same symbol in a row:
- I before V or X: IV (4), IX (9)
- X before L or C: XL (40), XC (90)
- C before D or M: CD (400), CM (900)

**Complexity:**

This algorithm is O(n) where n is the length of the Roman numeral string. Each character is examined exactly once, and dictionary lookups are O(1).

Space complexity is O(1) since we only use a constant amount of extra space regardless of input size.

</details>

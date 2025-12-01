# Read Aloud

Convert a number to its word equivalent.

## Task

Write a function `read_aloud(number)` that takes a string representation of a number (0-999) and returns the number spelled out in English words in uppercase.

- Convert numbers 0-999 to English words
- Return words in uppercase
- Return empty string for empty input
- Input will only contain digit characters

## Template

```python
ONES = {
    0: 'ZERO', 1: 'ONE', 2: 'TWO', 3: 'THREE', 4: 'FOUR',
    5: 'FIVE', 6: 'SIX', 7: 'SEVEN', 8: 'EIGHT', 9: 'NINE'
}

TEENS = {
    10: 'TEN', 11: 'ELEVEN', 12: 'TWELVE', 13: 'THIRTEEN', 14: 'FOURTEEN',
    15: 'FIFTEEN', 16: 'SIXTEEN', 17: 'SEVENTEEN', 18: 'EIGHTEEN', 19: 'NINETEEN'
}

TENS = {
    20: 'TWENTY', 30: 'THIRTY', 40: 'FORTY', 50: 'FIFTY',
    60: 'SIXTY', 70: 'SEVENTY', 80: 'EIGHTY', 90: 'NINETY'
}


def read_aloud(number: str) -> str:
    pass


if __name__ == "__main__":
    print(read_aloud("42"))  # "FORTY TWO"
    print(read_aloud("7"))  # "SEVEN"
    print(read_aloud("105"))  # "ONE HUNDRED FIVE"
    print(read_aloud("333"))  # "THREE HUNDRED THIRTY THREE"
    print(read_aloud(""))  # ""
    print(read_aloud("0"))  # "ZERO"
```

## Hint

<details>
<summary>Click to reveal hint</summary>

Use dictionaries to map numbers to words, then handle different cases:

```python
num = int(number)

if num == 0:
    return "ZERO"
if num < 10:
    return ONES[num]
if num < 20:
    return TEENS[num]
if num < 100:
    tens_digit = num // 10 * 10
    ones_digit = num % 10
    if ones_digit == 0:
        return TENS[tens_digit]
    else:
        return TENS[tens_digit] + " " + ONES[ones_digit]
```

For hundreds, extract the hundreds digit and process the remainder (0-99) recursively.

</details>

## Note

<details>
<summary>Click to reveal note</summary>

**Number ranges require different handling:**

- **0-9**: Direct lookup in ONES dictionary
- **10-19**: Direct lookup in TEENS dictionary (special cases)
- **20-99**: Combine TENS and ONES ("FORTY" + "TWO")
- **100-999**: Say hundreds digit + "HUNDRED" + remainder

The teens (10-19) are special because they don't follow the regular pattern - "eleven" is not "ten one", "twelve" is not "ten two", etc.

</details>

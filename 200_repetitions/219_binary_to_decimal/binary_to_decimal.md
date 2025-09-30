# Binary to Decimal

Convert a binary (base 2) number to decimal (base 10).

## Task
- Read a binary number from the user as a string
- Convert it to decimal by processing each digit
- Display the equivalent decimal number

## Examples
**Example 1:**
```
Enter a binary number: 1010
```
```
The decimal equivalent is 10
```

**Example 2:**
```
Enter a binary number: 1111
```
```
The decimal equivalent is 15
```

**Example 3:**
```
Enter a binary number: 10000
```
```
The decimal equivalent is 16
```

## Logic
- Binary to decimal conversion:
  - Each digit position represents a power of 2
  - Rightmost digit = 2⁰, next = 2¹, next = 2², etc.
  - Example: 1010₂ = 1×2³ + 0×2² + 1×2¹ + 0×2⁰ = 8 + 0 + 2 + 0 = 10

## Algorithm
- Initialize result = 0
- For each digit in the binary string:
  - Multiply result by 2
  - Add the current digit (0 or 1)
- Display result

## Hints
- Read as string to process digit by digit
- Convert each character to int: int(digit)
- Use loop to process each digit from left to right
- Alternative: result = result * 2 + digit
- Can also use int(binary_string, 2) but try the loop approach!

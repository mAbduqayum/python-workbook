# Decimal to Binary

Convert a decimal (base 10) number to binary (base 2).

## Task
- Read a decimal number from the user as an integer
- Use the division algorithm to convert to binary
- Display the binary representation

## Algorithm
1. Let result be an empty string
2. Let q represent the number to convert
3. Repeat:
   - Set r = remainder when q is divided by 2
   - Convert r to string and add to the BEGINNING of result
   - Divide q by 2 (floor division), store back into q
4. Until q is 0
5. Display result

## Examples
**Example 1:**
```
Enter a decimal number: 10
```
```
The binary equivalent is 1010
```

**Example 2:**
```
Enter a decimal number: 15
```
```
The binary equivalent is 1111
```

**Example 3:**
```
Enter a decimal number: 42
```
```
The binary equivalent is 101010
```

## Logic
- Decimal to binary uses repeated division by 2
- The remainders (0 or 1) form the binary digits
- Read remainders in reverse order (bottom to top)
- Example: 10 ÷ 2 = 5 R 0, 5 ÷ 2 = 2 R 1, 2 ÷ 2 = 1 R 0, 1 ÷ 2 = 0 R 1
- Reading bottom to top: 1010

## Hints
- Use q % 2 to get remainder
- Use q // 2 for floor division
- Add to beginning of string: result = str(r) + result
- Loop while q > 0
- Can also use bin() but try the algorithm approach!

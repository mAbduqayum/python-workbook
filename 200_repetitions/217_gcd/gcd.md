# Greatest Common Divisor

Find the greatest common divisor (GCD) of two positive integers.

## Task
- Read two positive integers n and m from the user
- Use the provided algorithm to find their GCD
- Display the result

## Algorithm
1. Initialize d to the smaller of m and n
2. While d does not evenly divide m OR d does not evenly divide n:
   - Decrease d by 1
3. Report d as the greatest common divisor

## Examples
**Example 1:**
```
Enter first number: 12
Enter second number: 8
```
```
The GCD is 4
```

**Example 2:**
```
Enter first number: 48
Enter second number: 18
```
```
The GCD is 6
```

**Example 3:**
```
Enter first number: 17
Enter second number: 19
```
```
The GCD is 1
```

## Logic
- The GCD is the largest number that divides both n and m evenly
- Start from the smaller number and work down
- First number that divides both evenly is the GCD

## Hints
- Use min(m, n) to find the smaller number
- Check divisibility: m % d == 0 and n % d == 0
- Loop while d does NOT divide both: while m % d != 0 or n % d != 0
- Decrease d by 1 in each iteration

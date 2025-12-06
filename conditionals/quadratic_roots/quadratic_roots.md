# Exercise: Roots of a Quadratic Function

Write a program that computes the real roots of a quadratic function using the quadratic formula.

## Task
- Read coefficients `a`, `b`, and `c` from the user
- Calculate the discriminant and determine the number of real roots
- Display the number of roots and their values in ascending order (if any)

## Quadratic Formula
For equation `ax² + bx + c = 0`:
- **Discriminant**: `𝚫 = b² - 4ac`
- **Roots**: `x = (-b ± √𝚫) / (2a)`

## Root Cases
- **`𝚫 < 0`**: No real roots
- **`𝚫 = 0`**: One real root
- **`𝚫 > 0`**: Two real roots

## Examples
**Example 1:** (Two roots)
```
1
-5
6
```
```
2 roots: 2.00 and 3.00
```

**Example 2:** (One root)
```
1
-4
4
```
```
1 root: 2.00
```

**Example 3:** (No real roots)
```
1
2
5
```
```
No real roots
```

**Example 4:** (Two roots)
```
2
-7
3
```
```
2 roots: 0.50 and 3.00
```

## Note
- Use `import math` for the square root function (`math.sqrt()`)

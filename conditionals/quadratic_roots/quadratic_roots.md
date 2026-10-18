# Exercise: Roots of a Quadratic Function

Write a program that computes the real roots of a quadratic function using the quadratic formula. Print each root with 2 decimal places; when there are two, print them on one line, smallest first, separated by a space.

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
2.00 3.00
```

**Example 2:** (One root)
```
1
-4
4
```
```
2.00
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

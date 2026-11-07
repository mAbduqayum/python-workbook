# Quadratic Roots

Write a function that calculates the roots of a quadratic equation.

You wrote this as a program in [Roots of a Quadratic Function](../../conditionals/quadratic_roots/quadratic_roots.md); now make it a function.

## Task
- Create a function `quadratic_roots(a, b, c)` for equation ax² + bx + c = 0
- Return a tuple `(root1, root2)` when there are two distinct real roots
- Return the single root when there is exactly one (repeated) root
- Return `None` when there are no real roots

## Examples

| Call                        | Returns      |
|-----------------------------|--------------|
| `quadratic_roots(1, -3, 2)` | `(2.0, 1.0)` |
| `quadratic_roots(1, -2, 1)` | `1.0`        |
| `quadratic_roots(1, 0, 1)`  | `None`       |

## Formula
- Discriminant: Δ = b² - 4ac
- If Δ < 0: no real roots
- If Δ = 0: one repeated root, -b / (2a)
- If Δ > 0: two roots, (-b + √Δ) / (2a) and (-b - √Δ) / (2a)


# GCD

Create a recursive function that calculates the greatest common divisor using Euclidean algorithm.

## Template

```python
def gcd(a: int, b: int) -> int:
    pass


if __name__ == "__main__":
    print(gcd(48, 18))   # 6
    print(gcd(18, 48))   # 6
    print(gcd(100, 25))  # 25
    print(gcd(17, 13))   # 1
```

<details>
<summary>Hint</summary>

- `gcd(a, 0) = a` (base case)
- `gcd(a, b) = gcd(b, a % b)` for b > 0
- Works even if b > a (first step swaps them)

</details>

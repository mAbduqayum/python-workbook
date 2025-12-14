# Power

Create a recursive function that calculates base raised to exponent.

## Template

```python
def power(base: int, exp: int) -> int:
    pass


if __name__ == "__main__":
    print(power(2, 0))   # 1
    print(power(2, 3))   # 8
    print(power(3, 4))   # 81
    print(power(10, 3))  # 1000
```

<details>
<summary>Hint</summary>

- `power(base, 0) = 1` (base case)
- `power(base, exp) = base × power(base, exp - 1)` for exp > 0

</details>

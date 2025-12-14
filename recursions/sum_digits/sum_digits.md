# Sum Digits

Create a recursive function that calculates the sum of digits in a number.

## Template

```python
def sum_digits(n: int) -> int:
    pass


if __name__ == "__main__":
    print(sum_digits(0))      # 0
    print(sum_digits(123))    # 6
    print(sum_digits(9999))   # 36
    print(sum_digits(-456))   # 15
```

<details>
<summary>Hint</summary>

- `sum_digits(n) = n` when n < 10 (base case)
- `sum_digits(n) = (n % 10) + sum_digits(n // 10)` for n >= 10
- Handle negative numbers by using absolute value

</details>

# Count Digits

Create a recursive function that counts the digits in a number.

## Template

```python
def count_digits(n: int) -> int:
    pass


if __name__ == "__main__":
    print(count_digits(0))       # 1
    print(count_digits(5))       # 1
    print(count_digits(123))     # 3
    print(count_digits(1000000)) # 7
```

<details>
<summary>Hint</summary>

- Single digit (0-9) has 1 digit (base case)
- `count_digits(n) = 1 + count_digits(n // 10)` for n >= 10
- Handle negative numbers by using absolute value

</details>

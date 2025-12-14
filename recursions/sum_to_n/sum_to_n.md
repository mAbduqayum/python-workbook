# Sum to N

Create a recursive function that calculates the sum from 1 to n.

For example: `sum_to_n(5) = 5 + 4 + 3 + 2 + 1 = 15`

## Template

```python
def sum_to_n(n: int) -> int:
    pass


if __name__ == "__main__":
    print(sum_to_n(1))   # 1
    print(sum_to_n(5))   # 15
    print(sum_to_n(10))  # 55
    print(sum_to_n(100)) # 5050
```

<details>
<summary>Hint</summary>

- `sum_to_n(1) = 1` (base case)
- `sum_to_n(n) = n + sum_to_n(n-1)` for n > 1

</details>

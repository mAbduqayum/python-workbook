# Factorial

Create a recursive function that calculates the factorial of a number.

Factorial of n (written as n!) is the product of all positive integers up to n. For example: `5! = 5 × 4 × 3 × 2 × 1 = 120`

## Template

```python
def factorial(n: int) -> int:
    pass


if __name__ == "__main__":
    print(factorial(0))   # 1
    print(factorial(1))   # 1
    print(factorial(5))   # 120
    print(factorial(10))  # 3628800
```

<details>
<summary>Hint</summary>

- `0! = 1` and `1! = 1` (base cases)
- `n! = n × (n-1)!` for n > 1

</details>

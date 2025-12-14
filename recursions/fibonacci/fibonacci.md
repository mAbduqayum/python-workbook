# Fibonacci

Create a recursive function that returns the nth Fibonacci number.

The Fibonacci sequence starts with 0 and 1, then each subsequent number is the sum of the two preceding ones: `0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...`

## Template

```python
def fibonacci(n: int) -> int:
    pass


if __name__ == "__main__":
    print(fibonacci(0))   # 0
    print(fibonacci(1))   # 1
    print(fibonacci(6))   # 8
    print(fibonacci(10))  # 55
```

<details>
<summary>Hint</summary>

- `fibonacci(0) = 0` (base case)
- `fibonacci(1) = 1` (base case)
- `fibonacci(n) = fibonacci(n-1) + fibonacci(n-2)` for n > 1

</details>

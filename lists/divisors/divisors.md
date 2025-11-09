# List Divisors

Return a list of all divisors of a given number.

## Task

- Create a function `list_divisors(n)` that takes an integer
- Return a list of all divisors of n in ascending order

## Template:

```python
def list_divisors(n: int) -> list[int]:
    pass


if __name__ == "__main__":
    # Test your function
    print(list_divisors(12))   # [1, 2, 3, 4, 6, 12]
    print(list_divisors(7))    # [1, 7]
    print(list_divisors(1))    # [1]
```

<details>
<summary><strong>Hint</strong></summary>

- Iterate through numbers from 1 to n
- Check if each number divides n evenly (n % i == 0)
- Add divisors to a list
- Use list comprehension: `[i for i in range(1, n+1) if n % i == 0]`

</details>

## Note

- A divisor is a number that divides n without a remainder
- 1 and n are always divisors of n
- The result should be sorted in ascending order

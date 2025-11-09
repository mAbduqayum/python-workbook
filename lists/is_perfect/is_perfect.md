# Is Perfect

Determine if a number is a perfect number.

## Task

- Create a function `is_perfect(n)` that takes a positive integer
- Return True if n is a perfect number, False otherwise
- A perfect number equals the sum of its proper divisors (excluding itself)

## Template:

```python
def is_perfect(n: int) -> bool:
    pass


if __name__ == "__main__":
    # Test your function
    print(is_perfect(6))  # True (1 + 2 + 3 = 6)
    print(is_perfect(28))  # True (1 + 2 + 4 + 7 + 14 = 28)
    print(is_perfect(12))  # False
```

<details>
<summary><strong>Hint</strong></summary>

- Find all divisors of n from 1 to n-1 (proper divisors)
- Sum the divisors
- Check if the sum equals n
- Use list comprehension: `sum([i for i in range(1, n) if n % i == 0]) == n`

</details>

## Note

- Perfect numbers are rare: 6, 28, 496, 8128, ...
- Proper divisors exclude the number itself
- 1 is not considered a perfect number

<details>
<summary><strong>Historical Note</strong></summary>

Perfect numbers have captivated mathematicians for over two millennia. Euclid proved around 300 BCE that if 2^p - 1 is prime (now called a Mersenne prime), then 2^(p-1) × (2^p - 1) is a perfect number. This elegant formula still generates all known even perfect numbers. As of 2024, only 52 perfect numbers have been discovered—the largest containing over 49 million digits. Whether any odd perfect numbers exist remains one of mathematics' oldest unsolved mysteries, spanning more than 2,000 years.

</details>

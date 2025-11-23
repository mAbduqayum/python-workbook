# Find Missing Numbers

Find which numbers are missing from a range.

## Task

Write a function `find_missing(numbers, n)` that takes a list of numbers and an upper bound `n`, and returns a list of
all numbers from 1 to `n` (inclusive) that are **not** in the input list.

- The result should be sorted in ascending order
- Duplicates in the input list should be ignored

## Template

```python
def find_missing(numbers: list, n: int) -> list:
    pass


if __name__ == "__main__":
    print(find_missing([1, 2, 4, 6], 6))  # [3, 5]
    print(find_missing([2, 3, 7, 8], 10))  # [1, 4, 5, 6, 9, 10]
    print(find_missing([1, 2, 3], 3))  # []
    print(find_missing([], 5))  # [1, 2, 3, 4, 5]
    print(find_missing([1, 1, 2, 2], 4))  # [3, 4]
```

## Hint

<details>
<summary>Click to reveal hint</summary>

Use set difference to find missing numbers:

```python
full_range = set(range(1, n + 1))
present = set(numbers)
missing = full_range - present
return sorted(missing)
```

</details>

## Note

<details>
<summary>Click to reveal note</summary>

This is a classic interview problem! The set-based solution runs in O(n) time.

An alternative approach without using extra space (for finding a **single** missing number) uses the mathematical
formula for the sum of 1 to n:

```python
expected_sum = n * (n + 1) // 2
actual_sum = sum(numbers)
missing = expected_sum - actual_sum
```

But for **multiple** missing numbers, the set approach is cleaner and more flexible.

</details>

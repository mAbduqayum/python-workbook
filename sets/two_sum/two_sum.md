# Two Sum

Check if two numbers in a list add up to a target value.

## Task

Write a function `has_two_sum(numbers, target)` that returns `True` if any two **different** numbers in the list add up
to the target, and `False` otherwise.

- The same element cannot be used twice
- There may be duplicate values in the list

## Template

```python
def has_two_sum(numbers: list, target: int) -> bool:
    pass


if __name__ == "__main__":
    print(has_two_sum([1, 2, 3, 4], 5))  # True (1+4 or 2+3)
    print(has_two_sum([1, 2, 3, 4], 10))  # False
    print(has_two_sum([3, 3], 6))  # True (3+3)
    print(has_two_sum([3], 6))  # False (can't use same element twice)
    print(has_two_sum([], 5))  # False
    print(has_two_sum([5, 0], 5))  # True (5+0)
```

## Hint

<details>
<summary>Click to reveal hint</summary>

For each number, calculate what value you'd need (the "complement") to reach the target, and check if you've seen it
before:

```python
seen = set()
for num in numbers:
    complement = target - num
    if complement in seen:
        return True
    seen.add(num)
return False
```

</details>

## Note

<details>
<summary>Click to reveal note</summary>

This is the **complement search** pattern, one of the most common interview questions!

The key insight: instead of checking every pair of numbers (O(n²)), we ask:
> "For each number, have I already seen the number that would complete the sum?"

This transforms an O(n²) nested loop into an O(n) single pass.

```python
# Naive O(n²) approach
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == target:
            return True

# Smart O(n) approach using sets
seen = set()
for num in numbers:
    if (target - num) in seen:
        return True
    seen.add(num)
```

</details>

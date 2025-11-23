# Longest Consecutive Sequence

Find the length of the longest sequence of consecutive numbers.

## Task

Write a function `longest_consecutive(numbers)` that finds the length of the longest sequence of consecutive integers in the list.

- The numbers don't need to be adjacent in the list
- The order of numbers in the list doesn't matter
- Return 0 for an empty list

## Template

```python
def longest_consecutive(numbers: list) -> int:
    pass


if __name__ == "__main__":
    print(longest_consecutive([100, 4, 200, 1, 3, 2]))  # 4 (sequence: 1,2,3,4)
    print(longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))  # 9 (sequence: 0-8)
    print(longest_consecutive([1, 2, 0, 1]))  # 3 (sequence: 0,1,2)
    print(longest_consecutive([]))  # 0
    print(longest_consecutive([5]))  # 1
    print(longest_consecutive([1, 3, 5, 7]))  # 1 (no consecutive numbers)
```

## Hint

<details>
<summary>Click to reveal hint</summary>

The key insight: only start counting from numbers that are the **beginning** of a sequence (i.e., `num - 1` is not in the set).

```python
num_set = set(numbers)
longest = 0

for num in num_set:
    # Only start counting if this is the start of a sequence
    if num - 1 not in num_set:
        current = num
        length = 1

        while current + 1 in num_set:
            current += 1
            length += 1

        longest = max(longest, length)

return longest
```

</details>

## Note

This is a classic **hard** interview problem that becomes elegant with sets.

**Why check `num - 1 not in num_set`?**

Without this optimization, we'd start counting from every number, leading to O(n²) time. By only starting from sequence beginnings, each number is visited at most twice (once in the outer loop, once in the while loop), giving us O(n) time.

**Example walkthrough with [100, 4, 200, 1, 3, 2]:**

```
num=100: 99 not in set → start sequence → 100 (length 1)
num=4:   3 in set → skip (not a sequence start)
num=200: 199 not in set → start sequence → 200 (length 1)
num=1:   0 not in set → start sequence → 1,2,3,4 (length 4) ← longest!
num=3:   2 in set → skip
num=2:   1 in set → skip

Answer: 4
```

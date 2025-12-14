# Binary Search

Create a recursive function that searches for a target in a sorted list.

## Template

```python
def binary_search(lst: list, target: int) -> int:
    pass


if __name__ == "__main__":
    nums = [1, 3, 5, 7, 9, 11]
    print(binary_search(nums, 7))   # 3
    print(binary_search(nums, 1))   # 0
    print(binary_search(nums, 11))  # 5
    print(binary_search(nums, 4))   # -1
```

<details>
<summary>Hint</summary>

- Return index if found, -1 if not found
- Use a helper function with low and high parameters
- Compare middle element with target
- Search left half if target < middle, right half if target > middle

</details>

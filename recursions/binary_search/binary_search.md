# Binary Search

Create a recursive function that searches for a target in a sorted list and returns its index, or `-1` if the target is not in the list.

## Template

```python
def binary_search(l: list, target: int) -> int:
    pass


if __name__ == "__main__":
    nums = [1, 3, 5, 7, 9, 11]
    print(binary_search(nums, 7))   # 3
    print(binary_search(nums, 1))   # 0
    print(binary_search(nums, 11))  # 5
    print(binary_search(nums, 4))   # -1
```

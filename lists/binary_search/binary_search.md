# Binary Search

Perform binary search on a sorted list to find an element.

## Task

- Create a function `binary_search(items, target)` that takes a sorted list and a target value
- Return the index of the target if found, -1 otherwise

## Template:

```python
def binary_search(items: list, target) -> int:
    pass


if __name__ == "__main__":
    # Test your function
    items = [1, 2, 3, 4, 5]
    print(binary_search(items, 3))  # 2
    print(binary_search(items, 6))  # -1
```

## Note

- Assume the list is sorted in ascending order
- Binary search has O(log n) time complexity
- More efficient than linear search for large sorted lists

<details>
<summary><strong>Historical Note</strong></summary>

The concept of searching through sorted data dates back to antiquity and is likely much older than our earliest evidence. The Inakibit-Anu tablet from Babylon (c. 200 BCE) is the oldest known example, containing sorted lists specifically organized for faster searching. Binary search was first mentioned in a computing context in 1946 by John Mauchly, but the first bug-free implementation wasn't published until 1962. Despite its apparent simplicity, implementing it correctly is notoriously difficult—when Jon Bentley assigned it to professional programmers, 90% failed to provide a correct solution after several hours, mainly due to rare edge cases.

</details>

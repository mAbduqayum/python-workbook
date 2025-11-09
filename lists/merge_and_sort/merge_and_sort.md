# Merge and Sort

Merge two sorted lists into one sorted list.

## Task

- Create a function `merge_and_sort(list1, list2)` that takes two sorted lists
- Return a new sorted list containing all elements from both lists

## Template:

```python
def merge_and_sort(list1: list[int], list2: list[int]) -> list[int]:
    pass


if __name__ == "__main__":
    # Test your function
    print(merge_and_sort([1, 3, 5], [2, 4, 6]))  # [1, 2, 3, 4, 5, 6]
    print(merge_and_sort([1, 2], [3, 4]))        # [1, 2, 3, 4]
```

<details>
<summary><strong>Hint</strong></summary>

- Concatenate both lists: `list1 + list2`
- Sort the result: `sorted(list1 + list2)`
- Or implement a merge algorithm that combines two sorted lists efficiently

</details>

## Note

- Both input lists are already sorted
- The simple approach is to concatenate and sort: O(n log n)
- An efficient merge algorithm would be O(n) but is more complex

<details>
<summary><strong>Historical Note</strong></summary>

The merge operation is the key component of merge sort, one of computer science's most elegant algorithms. Merge sort was invented by John von Neumann in 1945, making it one of the earliest sorting algorithms designed for computers. Von Neumann was a legendary polymath whose contributions spanned mathematics, physics, economics, and computer science. Beyond inventing merge sort, he worked on the Manhattan Project, pioneered game theory, and developed the stored-program computer architecture (the "von Neumann architecture") that remains the foundation of nearly all modern computers.

</details>

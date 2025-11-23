# List Intersection

Find common elements between two lists.

## Task

Write a function `list_intersection(list1, list2)` that returns a new list containing only the elements that appear in *
*both** input lists.

- Each element should appear only once in the result
- The order of elements does not need to be preserved

## Template

```python
def list_intersection(list1: list, list2: list) -> list:
    pass


if __name__ == "__main__":
    print(list_intersection([1, 2, 3, 4], [3, 4, 5, 6]))  # [3, 4] (order may vary)
    print(list_intersection(["a", "b", "c"], ["b", "c", "d"]))  # ['b', 'c'] (order may vary)
    print(list_intersection([1, 2], [3, 4]))  # []
    print(list_intersection([1, 1, 2, 2], [2, 2, 3, 3]))  # [2]
```

## Hint

<details>
<summary>Click to reveal hint</summary>

Use the set intersection operator `&` or the `.intersection()` method:

```python
set1 = set(list1)
set2 = set(list2)
return list(set1 & set2)
```

</details>

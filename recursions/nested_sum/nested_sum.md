# Nested Sum

Create a recursive function that calculates the sum of all numbers in a nested list.

## Template

```python
def nested_sum(lst: list) -> int:
    pass


if __name__ == "__main__":
    print(nested_sum([1, 2, 3]))              # 6
    print(nested_sum([1, [2, 3], 4]))         # 10
    print(nested_sum([1, [2, [3, [4]]]]))     # 10
    print(nested_sum([[1, 2], [3, [4, 5]]]))  # 15
```

<details>
<summary>Hint</summary>

- If element is a number, add it to total
- If element is a list, recursively sum it
- Use `isinstance(item, list)` to check if item is a list

</details>

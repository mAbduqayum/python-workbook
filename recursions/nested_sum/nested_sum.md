# Nested Sum

Create a recursive function that calculates the sum of all numbers in a nested list.

## Template

```python
def nested_sum(l: list) -> int:
    pass


if __name__ == "__main__":
    print(nested_sum([2, 3, 5]))               # 10
    print(nested_sum([2, [3, 5], 7]))          # 17
    print(nested_sum([2, [3, [5, [7]]]]))      # 17
    print(nested_sum([[2, 3], [5, [7, 11]]]))  # 28
```

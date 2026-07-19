# Flatten List

Create a recursive function that flattens a nested list.

## Template

```python
def flatten_list(l: list) -> list:
    pass


if __name__ == "__main__":
    print(flatten_list([2, 3, 5]))           # [2, 3, 5]
    print(flatten_list([2, [3, 5], 7]))      # [2, 3, 5, 7]
    print(flatten_list([[2, 3], [5, 7]]))    # [2, 3, 5, 7]
    print(flatten_list([2, [3, [5, [7]]]]))  # [2, 3, 5, 7]
```

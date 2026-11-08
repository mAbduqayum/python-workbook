# Nesting Depth

Create a recursive function that finds how deeply a list is nested.

A list with no lists inside has depth 1. Each level of lists inside adds 1, and
the deepest one counts.

## Template

```python
def max_depth(data: list) -> int:
    pass


if __name__ == "__main__":
    print(max_depth([1, 2, 3]))  # 1
    print(max_depth([1, [2, 3]]))  # 2
    print(max_depth([1, [2, [3]], [4]]))  # 3
    print(max_depth([]))  # 1
```

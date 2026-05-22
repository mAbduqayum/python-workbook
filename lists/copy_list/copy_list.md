# Copy List

Create a copy of a list using slicing and prove it's a different object.

## Task

- Create a function `copy_list(lst)` that takes a list
- Return a copy of the list (not the same object)
- Create a function `are_different_objects(lst1, lst2)` that checks if two lists are different objects

## Template:

```python
def copy_list(lst: list) -> list:
    pass


def are_different_objects(lst1: list, lst2: list) -> bool:
    pass


if __name__ == "__main__":
    # Test your functions
    original = [1, 2, 3, 4, 5]
    copied = copy_list(original)
    print(copied)  # [1, 2, 3, 4, 5]
    print(are_different_objects(original, copied))  # True
```

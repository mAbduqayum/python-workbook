# Filter Function

Implement a custom filter function that filters a list based on a callable condition.

## Task

- Create a function `filter_list(lst, condition)` that takes a list and a callable function
- Return a new list containing only elements that satisfy the condition
- The condition is a function that returns True or False

## Template:

```python
from typing import Callable


def filter_list(lst: list, condition: Callable) -> list:
    pass


if __name__ == "__main__":
    # Test your function
    def is_even(x):
        return x % 2 == 0


    print(filter_list([1, 2, 3, 4, 5, 6], is_even))  # [2, 4, 6]


    def is_positive(x):
        return x > 0


    print(filter_list([-2, -1, 0, 1, 2], is_positive))  # [1, 2]
```

<details>
<summary><strong>Hint</strong></summary>

- Iterate through the list
- For each element, call condition(element)
- If condition returns True, include the element in the result
- Use list comprehension: `[x for x in lst if condition(x)]`

</details>

## Note

- This mimics Python's built-in `filter()` function
- The condition parameter is a callable (function)
- You can use lambda functions as conditions

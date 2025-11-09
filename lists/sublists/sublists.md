# Sublists

Generate all possible sublists (contiguous subsequences) of a list.

## Task

- Create a function `sublists(lst)` that takes a list
- Return a list of all possible sublists (including empty list and full list)

## Template:

```python
def sublists(lst: list) -> list[list]:
    pass


if __name__ == "__main__":
    # Test your function
    print(sublists([1, 2, 3]))
    # [[], [1], [2], [3], [1, 2], [2, 3], [1, 2, 3]]
```

<details>
<summary><strong>Hint</strong></summary>

- Use nested loops to generate all sublists
- Outer loop: starting index (0 to len(lst))
- Inner loop: ending index (start to len(lst))
- For each pair (i, j), add lst[i:j] to result
- Include empty list: lst[0:0]

</details>

## Note

- A sublist is a contiguous subsequence
- Total number of sublists: n(n+1)/2 + 1 (including empty)
- Order doesn't matter for the test, but typically sorted by length then position

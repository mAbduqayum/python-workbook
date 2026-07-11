# Sublists

Generate all possible sublists (contiguous subsequences) of a list.

## Task

- Create a function `sublists(l)` that takes a list
- Return a list of all possible sublists (including empty list and full list)

## Template:

```python
def sublists(l: list) -> list[list]:
    pass


if __name__ == "__main__":
    # Test your function
    print(sublists([2, 3, 5]))
    # [[], [2], [3], [5], [2, 3], [3, 5], [2, 3, 5]]
```

<details>
<summary><strong>Hint</strong></summary>

- Use nested loops to generate all sublists
- Outer loop: starting index (0 to len(l))
- Inner loop: ending index (start to len(l))
- For each pair (i, j), add l[i:j] to result
- Include empty list: l[0:0]

</details>

## Note

- A sublist is a contiguous subsequence
- Total number of sublists: n(n+1)/2 + 1 (including empty)
- Order doesn't matter for the test, but typically sorted by length then position

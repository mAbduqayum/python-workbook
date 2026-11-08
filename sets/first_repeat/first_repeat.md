# First Repeat

Find the first word that appears for the second time.

## Task

Write a function `first_repeat(words)` that goes through a list of words in
order and returns the first word it has already seen, in lowercase.

- Case doesn't matter: `The` and `the` are the same word
- Return `""` if no word repeats

In `["red", "blue", "green", "blue", "red"]` the answer is `"blue"`: it comes
back first, even though `"red"` appears earlier.

## Template

```python
def first_repeat(words: list[str]) -> str:
    pass


if __name__ == "__main__":
    print(first_repeat(["The", "cat", "saw", "the", "dog"]))  # the
    print(first_repeat(["red", "blue", "green", "blue", "red"]))  # blue
    print(first_repeat(["one", "two", "three"]))  # ""
```

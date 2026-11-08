# Distinct Words

Count how many different words a text has.

## Task

Write a function `distinct_words(text)` that returns the number of different
words in `text`.

- Case doesn't matter: `The` and `the` are the same word

## Template

```python
def distinct_words(text: str) -> int:
    pass


if __name__ == "__main__":
    print(distinct_words("the cat and the hat"))  # 4
    print(distinct_words("The the THE"))  # 1
    print(distinct_words(""))  # 0
```

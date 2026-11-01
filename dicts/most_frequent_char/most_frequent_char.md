# Most Frequent Character

Find the character that appears most often in a string.

## Task

Write a function `most_frequent_char(text)` that returns the character that appears most frequently in the string.

- If several characters tie for the highest count, return any of them
- Counting is case-sensitive
- Count every character, including spaces and punctuation
- Return an empty string if `text` is empty

## Template

```python
def most_frequent_char(text: str) -> str:
    pass


if __name__ == "__main__":
    print(most_frequent_char("hello"))  # 'l'
    print(most_frequent_char("aabbcc"))  # 'a' (or 'b' or 'c' - all tied)
    print(most_frequent_char("AaA"))  # 'A'
```

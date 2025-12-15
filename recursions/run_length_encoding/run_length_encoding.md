# Run-Length Encoding

Create a recursive function that encodes a string using run-length encoding.

Run-length encoding compresses consecutive identical characters by storing the count followed by the character. For example, "AAABBC" becomes "3A2B1C".

## Template

```python
def run_length_encode(text: str) -> str:
    pass


if __name__ == "__main__":
    print(run_length_encode("AAABBC"))       # "3A2B1C"
    print(run_length_encode("Hello"))        # "1H1e2l1o"
    print(run_length_encode("XXXXX"))        # "5X"
    print(run_length_encode(""))             # ""
    print(run_length_encode("AABBBCCCC"))    # "2A3B4C"
```

<details>
<summary>Hint</summary>

- Base case: empty string returns empty string
- Count consecutive occurrences of the first character
- Create encoding for that run: count + character
- Recursively encode the rest of the string (after the run)
- Concatenate results

</details>

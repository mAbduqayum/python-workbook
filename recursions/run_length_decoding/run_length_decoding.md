# Run-Length Decoding

Create a recursive function that decodes a run-length encoded string.

Run-length encoding represents consecutive identical characters as a count followed by the character. For example, "AAABBC" is encoded as "3A2B1C".

## Template

```python
def run_length_decode(encoded: str) -> str:
    pass


if __name__ == "__main__":
    print(run_length_decode("3A2B1C"))      # "AAABBC"
    print(run_length_decode("1H1e1l1l1o"))  # "Hello"
    print(run_length_decode("5X"))          # "XXXXX"
    print(run_length_decode(""))            # ""
    print(run_length_decode("12A3B"))       # "AAAAAAAAAAAABBB"
```

<details>
<summary>Hint</summary>

- Base case: empty string returns empty string
- Parse the count (may be multiple digits) from the start
- Get the character after the count
- Repeat the character count times
- Recursively decode the rest of the string
- Concatenate results

</details>

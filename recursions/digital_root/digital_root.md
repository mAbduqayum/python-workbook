# Digital Root

Create a recursive function that keeps adding a natural number's digits until one
digit is left.

You added a number's digits once in [Sum Digits](../sum_digits/sum_digits.md); now keep going until the result is a single digit.

For 9875: 9 + 8 + 7 + 5 = 29, then 2 + 9 = 11, then 1 + 1 = 2.

## Template

```python
def digital_root(n: int) -> int:
    pass


if __name__ == "__main__":
    print(digital_root(9875))  # 2
    print(digital_root(38))  # 2
    print(digital_root(7))  # 7
```

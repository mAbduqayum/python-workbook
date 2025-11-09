# String to Integers

Create a function to convert string of integers into a list of integers.

## Template:

```python
def str_to_ints(string: str) -> list[int]:
    pass


if __name__ == "__main__":
    # Test your function
    print(str_to_ints("1 2 3 4 5"))  # [1, 2, 3, 4, 5]
    print(str_to_ints("10 -5 3"))    # [10, -5, 3]
    print(str_to_ints(""))           # []
```

## Note

- Assume the string contains valid integers separated by spaces
- The function should return an empty list if the string is empty

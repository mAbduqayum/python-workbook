# Is Integer

Write a function that determines if a string represents a valid integer.

## Task
- Create a function `is_int(s)` that takes a string
- Return `True` if the string represents a valid integer, `False` otherwise

## Function Signature
```python
def is_int(s: str) -> bool:
    pass
```

## Examples
```python
is_int("123")       # True
is_int("-456")      # True
is_int("0")         # True
is_int("12.5")      # False
is_int("abc")       # False
is_int("")          # False
is_int("+789")      # True
is_int("12a")       # False
```

## Logic
- Valid integers can start with an optional sign (+ or -)
- Rest of the string must be digits only
- Empty strings are not valid
- Leading/trailing spaces should make it invalid (be strict)

## Note
- Don't use built-in conversion functions like `int()`
- Check the string character by character
- Consider edge cases like empty strings and single characters

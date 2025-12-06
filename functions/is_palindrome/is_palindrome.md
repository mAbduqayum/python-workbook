# Is Palindrome

Write a function that determines if a string is a palindrome.

## Task
- Create a function `is_palindrome(s)` that takes a string
- Return `True` if it reads the same forwards and backwards, `False` otherwise

## Template:
```python
def is_palindrome(s: str) -> bool:
    pass


if __name__ == "__main__":
    # Test your function
    print(is_palindrome("racecar"))     # True
    print(is_palindrome("hello"))       # False
    print(is_palindrome("madam"))       # True
    print(is_palindrome("A"))           # True
    print(is_palindrome(""))            # True
    print(is_palindrome("noon"))        # True
    print(is_palindrome("abc"))         # False
```

## Logic
- Compare the string with its reverse
- Can use string slicing: `s[::-1]`
- Or compare characters from both ends moving inward

## Note
- Empty string is considered a palindrome
- Case-sensitive (for this version)
- Single character is a palindrome

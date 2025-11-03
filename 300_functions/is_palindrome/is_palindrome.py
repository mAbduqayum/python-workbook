def is_palindrome(s: str) -> bool:
    return s == s[::-1]


if __name__ == "__main__":
    # Test your function
    is_palindrome("racecar")     # True
    is_palindrome("hello")       # False
    is_palindrome("madam")       # True
    is_palindrome("A")           # True
    is_palindrome("")            # True
    is_palindrome("noon")        # True
    is_palindrome("abc")         # False

def is_palindrome(s: str) -> bool:
    return s == s[::-1]


if __name__ == "__main__":
    # Test your function
    print(is_palindrome("racecar"))  # True
    print(is_palindrome("hello"))  # False
    print(is_palindrome("madam"))  # True
    print(is_palindrome("A"))  # True
    print(is_palindrome(""))  # True
    print(is_palindrome("noon"))  # True
    print(is_palindrome("abc"))  # False

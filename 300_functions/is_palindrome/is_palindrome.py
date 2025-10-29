def is_palindrome(s: str) -> bool:
    """
    Determine if a string is a palindrome.
    
    Args:
        s: A string to check
        
    Returns:
        True if string is a palindrome, False otherwise
    """
    return s == s[::-1]

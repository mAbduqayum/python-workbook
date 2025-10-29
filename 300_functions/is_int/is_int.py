def is_int(s: str) -> bool:
    """
    Determine if a string represents a valid integer.
    
    Args:
        s: A string to check
        
    Returns:
        True if string represents a valid integer, False otherwise
    """
    if not s:
        return False
    
    start = 0
    if s[0] in "+-":
        start = 1
        if len(s) == 1:
            return False
    
    for i in range(start, len(s)):
        if not s[i].isdigit():
            return False
    
    return True

def to_base(n: int, base: int) -> str:
    """
    Convert a decimal number to any base (2-36).
    
    Args:
        n: A decimal integer
        base: The target base (2-36)
        
    Returns:
        The representation in the target base as a string
    """
    if n == 0:
        return "0"
    
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    
    while n > 0:
        result = digits[n % base] + result
        n //= base
    
    return result

def decimal_hex(n: int) -> str:
    """
    Convert a decimal number to hexadecimal string.
    
    Args:
        n: A decimal integer
        
    Returns:
        The hexadecimal representation as a string
    """
    if n == 0:
        return "0"
    
    hex_digits = "0123456789ABCDEF"
    hex_str = ""
    
    while n > 0:
        hex_str = hex_digits[n % 16] + hex_str
        n //= 16
    
    return hex_str

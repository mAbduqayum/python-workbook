def decimal_to_binary(n: int) -> str:
    """
    Convert a decimal number to binary string.
    
    Args:
        n: A decimal integer
        
    Returns:
        The binary representation as a string
    """
    if n == 0:
        return "0"
    
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n //= 2
    
    return binary

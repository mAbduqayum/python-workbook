def binary_to_decimal(binary: str) -> int:
    """
    Convert a binary string to decimal.
    
    Args:
        binary: A binary string (e.g., "1010")
        
    Returns:
        The decimal equivalent
    """
    decimal = 0
    power = 0
    
    for i in range(len(binary) - 1, -1, -1):
        if binary[i] == '1':
            decimal += 2 ** power
        power += 1
    
    return decimal

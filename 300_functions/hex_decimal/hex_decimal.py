def hex_decimal(hex_str: str) -> int:
    """
    Convert a hexadecimal string to decimal.
    
    Args:
        hex_str: A hexadecimal string (e.g., "1A")
        
    Returns:
        The decimal equivalent
    """
    decimal = 0
    power = 0
    
    for i in range(len(hex_str) - 1, -1, -1):
        digit = hex_str[i].upper()
        if digit.isdigit():
            value = int(digit)
        else:
            value = ord(digit) - ord('A') + 10
        
        decimal += value * (16 ** power)
        power += 1
    
    return decimal

def digit_sum(n: int) -> int:
    """
    Calculate the sum of digits in an integer.
    
    Args:
        n: An integer
        
    Returns:
        Sum of all digits in n
    """
    n = abs(n)
    total = 0
    
    while n > 0:
        total += n % 10
        n //= 10
    
    return total

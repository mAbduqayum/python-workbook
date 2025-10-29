def is_prime(n: int) -> bool:
    """
    Determine if a number is prime.
    
    Args:
        n: An integer to check
        
    Returns:
        True if n is prime, False otherwise
    """
    if n < 2:
        return False
    
    if n == 2:
        return True
    
    if n % 2 == 0:
        return False
    
    # Check odd divisors up to sqrt(n)
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    
    return True

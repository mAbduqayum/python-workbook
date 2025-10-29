def normalize_fraction(numerator: int, denominator: int) -> tuple[int, int]:
    """
    Normalize (simplify) a fraction to its lowest terms.
    
    Args:
        numerator: The numerator
        denominator: The denominator
        
    Returns:
        Tuple of (simplified_numerator, simplified_denominator)
    """
    if numerator == 0:
        return (0, 1)
    
    # Find GCD using Euclidean algorithm
    a, b = abs(numerator), abs(denominator)
    while b != 0:
        a, b = b, a % b
    gcd = a
    
    return (numerator // gcd, denominator // gcd)

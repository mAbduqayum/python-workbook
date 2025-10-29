import math


def quadratic_roots(a: float, b: float, c: float) -> tuple[float, float] | None:
    """
    Calculate the roots of a quadratic equation ax² + bx + c = 0.
    
    Args:
        a: Coefficient of x²
        b: Coefficient of x
        c: Constant term
        
    Returns:
        Tuple of (root1, root2) or None if no real roots exist
    """
    discriminant = b ** 2 - 4 * a * c
    
    if discriminant < 0:
        return None
    
    sqrt_discriminant = math.sqrt(discriminant)
    root1 = (-b + sqrt_discriminant) / (2 * a)
    root2 = (-b - sqrt_discriminant) / (2 * a)
    
    return (root1, root2)

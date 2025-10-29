def is_valid_triangle(a: float, b: float, c: float) -> bool:
    """
    Determine if three sides can form a valid triangle.
    
    Args:
        a: First side length
        b: Second side length
        c: Third side length
        
    Returns:
        True if sides can form a valid triangle, False otherwise
    """
    if a <= 0 or b <= 0 or c <= 0:
        return False
    return (a + b > c) and (a + c > b) and (b + c > a)

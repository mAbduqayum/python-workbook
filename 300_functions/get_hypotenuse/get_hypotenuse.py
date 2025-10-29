import math


def get_hypotenuse(a: float, b: float) -> float:
    """
    Calculate the hypotenuse of a right triangle.
    
    Args:
        a: One side of the right triangle
        b: Another side of the right triangle
        
    Returns:
        The length of the hypotenuse
    """
    return math.sqrt(a ** 2 + b ** 2)

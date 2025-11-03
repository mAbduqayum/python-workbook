import math


def quadratic_roots(a: float, b: float, c: float) -> tuple[float, float] | None:
    discriminant = b ** 2 - 4 * a * c
    
    if discriminant < 0:
        return None
    
    sqrt_discriminant = math.sqrt(discriminant)
    root1 = (-b + sqrt_discriminant) / (2 * a)
    root2 = (-b - sqrt_discriminant) / (2 * a)
    
    return root1, root2


if __name__ == "__main__":
    # Test your function
    quadratic_roots(1, -3, 2)     # (2.0, 1.0)
    quadratic_roots(1, 0, -4)     # (2.0, -2.0)
    quadratic_roots(1, -2, 1)     # (1.0, 1.0)
    quadratic_roots(1, 0, 1)      # None

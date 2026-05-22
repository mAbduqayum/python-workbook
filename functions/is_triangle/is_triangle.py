def is_triangle(a: float, b: float, c: float) -> bool:
    return abs(a - b) < c < a + b


if __name__ == "__main__":
    # Test your function
    print(is_triangle(3, 4, 5))  # True
    print(is_triangle(1, 2, 3))  # False
    print(is_triangle(5, 5, 5))  # True
    print(is_triangle(1, 1, 10))  # False
    print(is_triangle(7, 10, 5))  # True

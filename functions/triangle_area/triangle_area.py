def triangle_area(base: float, height: float) -> float:
    return (base * height) / 2


if __name__ == "__main__":
    # Test your function
    triangle_area(10, 5)  # 25.0
    triangle_area(6, 8)  # 24.0
    triangle_area(7.5, 4)  # 15.0
    triangle_area(1, 1)  # 0.5

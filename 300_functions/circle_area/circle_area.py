import math


def circle_area(radius: float) -> float:
    return math.pi * radius ** 2


if __name__ == "__main__":
    # Test your function
    circle_area(1)     # 3.141592653589793
    circle_area(2)     # 12.566370614359172
    circle_area(5)     # 78.53981633974483
    circle_area(10)    # 314.1592653589793

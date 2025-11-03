import math


def get_hypotenuse(a: float, b: float) -> float:
    return math.sqrt(a ** 2 + b ** 2)


if __name__ == "__main__":
    # Test your function
    get_hypotenuse(3, 4)      # 5.0
    get_hypotenuse(5, 12)     # 13.0
    get_hypotenuse(8, 15)     # 17.0
    get_hypotenuse(1, 1)      # 1.4142135623730951

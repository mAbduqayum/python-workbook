def bmi(weight: float, height: float) -> float:
    return weight / (height**2)


if __name__ == "__main__":
    # Test your function
    print(bmi(70, 1.75))  # 22.857142857142858
    print(bmi(80, 1.80))  # 24.691358024691358
    print(bmi(50, 1.60))  # 19.53125
    print(bmi(90, 1.75))  # 29.387755102040817

def fahrenheit_to_celsius(fahrenheit: float) -> float:
    return (fahrenheit - 32) * 5 / 9


if __name__ == "__main__":
    # Test your function
    fahrenheit_to_celsius(32)  # 0.0
    fahrenheit_to_celsius(212)  # 100.0
    fahrenheit_to_celsius(98.6)  # 37.0
    fahrenheit_to_celsius(-40)  # -40.0
    fahrenheit_to_celsius(0)  # -17.77777777777778

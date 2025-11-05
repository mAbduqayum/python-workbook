# BMI Calculator

Write a function that calculates Body Mass Index (BMI).

## Task
- Create a function `bmi(weight, height)` 
- Weight is in kilograms, height is in meters
- Return the BMI value

## Template:
```python
def bmi(weight: float, height: float) -> float:
    pass


if __name__ == "__main__":
    # Test your function
    print(bmi(70, 1.75))     # 22.857142857142858
    print(bmi(80, 1.80))     # 24.691358024691358
    print(bmi(50, 1.60))     # 19.53125
    print(bmi(90, 1.75))     # 29.387755102040817
```

## Formula
- BMI = weight / height²

## Note
- Weight should be in kilograms
- Height should be in meters
- Both parameters should be positive
- Return value should be a float

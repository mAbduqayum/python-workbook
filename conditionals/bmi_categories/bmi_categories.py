height = float(input())
weight = float(input())

bmi = weight / (height**2)

if bmi < 18.5:
    print("underweight")
elif bmi < 25.0:
    print("normal weight")
elif bmi < 30.0:
    print("overweight")
else:
    print("obese")

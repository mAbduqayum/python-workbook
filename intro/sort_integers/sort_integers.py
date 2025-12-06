num1 = int(input("Enter first integer: "))
num2 = int(input("Enter second integer: "))
num3 = int(input("Enter third integer: "))
min_num = min(num1, num2, num3)
max_num = max(num1, num2, num3)
mid_num = (num1 + num2 + num3) - min_num - max_num
print(f"Sorted order: {min_num}, {mid_num}, {max_num}")

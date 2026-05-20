num1 = int(input())
num2 = int(input())
num3 = int(input())
min_num = min(num1, num2, num3)
max_num = max(num1, num2, num3)
mid_num = (num1 + num2 + num3) - min_num - max_num
print(f"{min_num}, {mid_num}, {max_num}")

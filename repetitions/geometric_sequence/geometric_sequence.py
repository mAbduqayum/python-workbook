start = float(input())
ratio = float(input())
count = int(input())

current = start
for _ in range(count):
    print(current)
    current *= ratio

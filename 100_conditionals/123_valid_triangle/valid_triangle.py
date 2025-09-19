a = int(input())
b = int(input())
c = int(input())

if abs(a - b) < c < (a + b):
    print("valid triangle")
else:
    print("invalid triangle")

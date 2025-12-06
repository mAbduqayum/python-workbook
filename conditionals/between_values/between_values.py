a = int(input())
b = int(input())
c = int(input())

if a <= c:
    if a <= b <= c:
        print("between")
    else:
        print("not between")
else:
    if c <= b <= a:
        print("between")
    else:
        print("not between")

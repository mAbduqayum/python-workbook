n = int(input())
k = int(input())

remainder = n % k
if remainder == 0:
    print(n)
else:
    print(n + k - remainder)

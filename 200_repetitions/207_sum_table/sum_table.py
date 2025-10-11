n = int(input())

for row in range(n + 1):
    for col in range(n + 1):
        value = row + col
        print(f"{value:2}", end="")
        if col < n:
            print(" ", end="")
    print()

for row in range(10):
    for col in range(10):
        value = row + col
        print(f"{value:2}", end="")
        if col < 9:
            print(" ", end="")
    print()

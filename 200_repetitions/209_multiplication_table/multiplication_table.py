# Print header row
print("   ", end="")
for i in range(1, 11):
    print(f"{i:4}", end="")
print()

# Print each row
for row in range(1, 11):
    print(f"{row:2} ", end="")
    for col in range(1, 11):
        product = row * col
        print(f"{product:4}", end="")
    print()

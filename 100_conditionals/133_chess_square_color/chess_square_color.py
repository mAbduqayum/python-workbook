position = input()

column = position[0]
row = int(position[1])

# Convert column letter to number (a=1, b=2, ..., h=8)
column_num = ord(column) - ord('a') + 1

# Calculate if sum is even or odd
if (column_num + row) % 2 == 0:
    print("black")
else:
    print("white")
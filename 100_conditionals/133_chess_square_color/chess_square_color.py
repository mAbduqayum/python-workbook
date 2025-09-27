position = input()

col_str, row_str = position
row = int(row_str)

# Convert column letter to number (a=1, b=2, ..., h=8)
column_num = ord(col_str) - ord('a') + 1

# Calculate if sum is even or odd
if (column_num + row) % 2 == 0:
    print("black")
else:
    print("white")
position = input()

column_char, row_char = position

# Convert column letter to number (a=1, b=2, ..., h=8)
column_num = ord(column_char) - ord('a') + 1
row_num = int(row_char)

# Calculate if the sum is even or odd
if (column_num + row_num) % 2 == 0:
    print("black")
else:
    print("white")

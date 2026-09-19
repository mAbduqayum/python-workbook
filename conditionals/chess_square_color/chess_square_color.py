position = input()

column_letter, row_str = position
row = int(row_str)

column = ord(column_letter) - ord("a") + 1

# a1 (column 1, row 1) is black, and the color flips every square,
# so an even column + row means black
if (column + row) % 2 == 0:
    print("black")
else:
    print("white")

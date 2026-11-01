message = input()
shift = int(input())

result = ""

for char in message:
    if char.isalpha():
        if char.isupper():
            base = ord("A")
        else:
            base = ord("a")
        pos = ord(char) - base
        new_pos = (pos + shift) % 26
        result += chr(new_pos + base)
    else:
        result += char

print(result)

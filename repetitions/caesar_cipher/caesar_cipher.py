message = input()
shift = int(input())

result = ""

for char in message:
    if char.isalpha():
        if char.isupper():
            pos = ord(char) - ord("A")
            new_pos = (pos + shift) % 26
            result += chr(new_pos + ord("A"))
        else:
            pos = ord(char) - ord("a")
            new_pos = (pos + shift) % 26
            result += chr(new_pos + ord("a"))
    else:
        result += char

print(result)

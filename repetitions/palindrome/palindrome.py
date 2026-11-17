string = input()

is_palindrome = True
for i in range(len(string) // 2):
    if string[i] != string[-(i + 1)]:
        is_palindrome = False
        break

if is_palindrome:
    print("palindrome")
else:
    print("not a palindrome")

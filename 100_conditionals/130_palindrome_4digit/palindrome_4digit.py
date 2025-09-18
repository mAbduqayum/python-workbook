n = int(input())

# Extract digits
first_digit = n // 1000
second_digit = (n // 100) % 10
third_digit = (n // 10) % 10
fourth_digit = n % 10

if first_digit == fourth_digit and second_digit == third_digit:
    print("palindrome")
else:
    print("not palindrome")
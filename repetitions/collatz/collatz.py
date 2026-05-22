# Read first number
n = int(input())

# Loop until user enters n <= 0
while n > 0:
    # Display the sequence starting with n, one number per line
    print(n)

    # Generate sequence until reaching 1
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
        print(n)

    # Read next number
    n = int(input())

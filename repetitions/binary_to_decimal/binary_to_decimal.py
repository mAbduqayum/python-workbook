# Read binary number as string
binary = input()

# Initialize result
result = 0

# Process each digit
for digit in binary:
    result = result * 2 + int(digit)

# Display result
print(result)

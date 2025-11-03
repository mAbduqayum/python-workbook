def number_of_digits(n: int) -> int:
    if n == 0:
        return 1
    
    n = abs(n)
    count = 0
    
    while n > 0:
        count += 1
        n //= 10
    
    return count


if __name__ == "__main__":
    # Test your function
    number_of_digits(123)       # 3
    number_of_digits(0)         # 1
    number_of_digits(-456)      # 3
    number_of_digits(1000000)   # 7
    number_of_digits(7)         # 1

def digit_sum(n: int) -> int:
    n = abs(n)
    total = 0
    
    while n > 0:
        total += n % 10
        n //= 10
    
    return total


if __name__ == "__main__":
    # Test your function
    digit_sum(123)       # 6
    digit_sum(0)         # 0
    digit_sum(-456)      # 15
    digit_sum(1000)      # 1
    digit_sum(99)        # 18

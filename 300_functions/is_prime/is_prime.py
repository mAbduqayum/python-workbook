def is_prime(n: int) -> bool:
    if n < 2:
        return False
    
    if n == 2:
        return True
    
    if n % 2 == 0:
        return False
    
    # Check odd divisors up to sqrt(n)
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    
    return True


if __name__ == "__main__":
    # Test your function
    is_prime(2)       # True
    is_prime(17)      # True
    is_prime(1)       # False
    is_prime(4)       # False
    is_prime(29)      # True
    is_prime(0)       # False
    is_prime(-5)      # False

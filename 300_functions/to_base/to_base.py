def to_base(n: int, base: int) -> str:
    if n == 0:
        return "0"
    
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    
    while n > 0:
        result = digits[n % base] + result
        n //= base
    
    return result


if __name__ == "__main__":
    # Test your function
    to_base(10, 2)       # "1010"
    to_base(255, 16)     # "FF"
    to_base(8, 8)        # "10"
    to_base(100, 5)      # "400"
    to_base(0, 10)       # "0"

def decimal_hex(n: int) -> str:
    if n == 0:
        return "0"
    
    hex_digits = "0123456789ABCDEF"
    hex_str = ""
    
    while n > 0:
        hex_str = hex_digits[n % 16] + hex_str
        n //= 16
    
    return hex_str


if __name__ == "__main__":
    # Test your function
    decimal_hex(10)       # "A"
    decimal_hex(255)      # "FF"
    decimal_hex(16)       # "10"
    decimal_hex(26)       # "1A"
    decimal_hex(0)        # "0"

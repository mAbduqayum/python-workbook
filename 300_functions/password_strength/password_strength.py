def password_strength(pwd: str) -> str:
    """
    Evaluate password strength.
    
    Args:
        pwd: The password to evaluate
        
    Returns:
        Strength rating: "weak", "medium", or "strong"
    """
    length = len(pwd)
    
    # Count character types
    has_lower = any(c.islower() for c in pwd)
    has_upper = any(c.isupper() for c in pwd)
    has_digit = any(c.isdigit() for c in pwd)
    has_special = any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in pwd)
    
    char_types = sum([has_lower, has_upper, has_digit, has_special])
    
    # Evaluate strength
    if length >= 12 and char_types >= 3:
        return "strong"
    elif length >= 8 and char_types >= 2:
        return "medium"
    else:
        return "weak"

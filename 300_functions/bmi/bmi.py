def bmi(weight: float, height: float) -> float:
    """
    Calculate Body Mass Index (BMI).
    
    Args:
        weight: Weight in kilograms
        height: Height in meters
        
    Returns:
        BMI value
    """
    return weight / (height ** 2)

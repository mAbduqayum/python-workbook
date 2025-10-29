# Fahrenheit to Celsius

Write a function that converts Fahrenheit to Celsius.

## Task
- Create a function `fahrenheit_to_celsius(fahrenheit)` 
- Return the temperature in Celsius

## Function Signature
```python
def fahrenheit_to_celsius(fahrenheit: float) -> float:
    pass
```

## Examples
```python
fahrenheit_to_celsius(32)     # 0.0
fahrenheit_to_celsius(212)    # 100.0
fahrenheit_to_celsius(98.6)   # 37.0
fahrenheit_to_celsius(-40)    # -40.0
fahrenheit_to_celsius(0)      # -17.77777777777778
```

## Formula
- Celsius = (Fahrenheit - 32) × 5/9

## Note
- Return value should be a float
- Both positive and negative temperatures are valid

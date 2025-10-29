# Is Prime

Write a function that determines if a number is prime.

## Task
- Create a function `is_prime(n)` that takes an integer
- Return `True` if the number is prime, `False` otherwise

## Function Signature
```python
def is_prime(n: int) -> bool:
    pass
```

## Examples
```python
is_prime(2)       # True
is_prime(17)      # True
is_prime(1)       # False
is_prime(4)       # False
is_prime(29)      # True
is_prime(0)       # False
is_prime(-5)      # False
```

## Logic
- A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself
- Numbers less than 2 are not prime
- 2 is the only even prime number
- To check if n is prime, test divisibility from 2 to √n

## Note
- 1 is not considered a prime number
- 2 is the smallest prime number
- Negative numbers are not prime
- Optimize by only checking up to the square root of n

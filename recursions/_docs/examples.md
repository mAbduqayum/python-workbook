# Recursion Examples

## Example 1: Factorial

**Question:** What is 5!?

**Thinking:**
- 5! = 5 × 4!
- 4! = 4 × 3!
- 3! = 3 × 2!
- 2! = 2 × 1!
- 1! = 1

**Solution:**
```python
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # 120
```

---

## Example 2: Sum to N

**Question:** What is 1 + 2 + 3 + 4 + 5?

**Thinking:**
- sum(5) = 5 + sum(4)
- sum(4) = 4 + sum(3)
- sum(3) = 3 + sum(2)
- sum(2) = 2 + sum(1)
- sum(1) = 1

**Solution:**
```python
def sum_to_n(n):
    if n == 1:
        return 1
    return n + sum_to_n(n - 1)

print(sum_to_n(5))  # 15
```

---

## Example 3: Count Digits

**Question:** How many digits in 12345?

**Thinking:**
- 12345 has same digits as 1234, plus one more
- 1234 has same digits as 123, plus one more
- ...
- Single digit (0-9) has 1 digit

**Solution:**
```python
def count_digits(n):
    n = abs(n)
    if n < 10:
        return 1
    return 1 + count_digits(n // 10)

print(count_digits(12345))  # 5
```

---

## Example 4: Sum of Digits

**Question:** What is 1+2+3+4+5 for number 12345?

**Thinking:**
- Sum of 12345 = 5 + sum of 1234
- Sum of 1234 = 4 + sum of 123
- ...
- Sum of single digit = itself

**Solution:**
```python
def sum_digits(n):
    n = abs(n)
    if n < 10:
        return n
    return (n % 10) + sum_digits(n // 10)

print(sum_digits(12345))  # 15
```

---

## Example 5: Power

**Question:** What is 2^5?

**Thinking:**
- 2^5 = 2 × 2^4
- 2^4 = 2 × 2^3
- ...
- 2^0 = 1

**Solution:**
```python
def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp - 1)

print(power(2, 5))  # 32
```

---

## Example 6: Fibonacci

**Question:** What is the 6th Fibonacci number?

**Thinking:**
- fib(6) = fib(5) + fib(4)
- fib(5) = fib(4) + fib(3)
- ...
- fib(1) = 1
- fib(0) = 0

**Solution:**
```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))  # 8
```

---

## Example 7: GCD (Euclidean Algorithm)

**Question:** What is GCD of 48 and 18?

**Thinking:**
- gcd(48, 18) = gcd(18, 48 % 18) = gcd(18, 12)
- gcd(18, 12) = gcd(12, 18 % 12) = gcd(12, 6)
- gcd(12, 6) = gcd(6, 12 % 6) = gcd(6, 0)
- gcd(6, 0) = 6

**What if b > a?** It still works!
- gcd(18, 48) = gcd(48, 18 % 48) = gcd(48, 18)
- Then continues as normal

**Solution:**
```python
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

print(gcd(48, 18))  # 6
print(gcd(18, 48))  # 6 (same result!)
```

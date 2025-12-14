# Recursion vs Iteration

Every recursion can be written as a loop, and vice versa.

## Factorial

**Recursive:**
```python
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)
```

**Iterative:**
```python
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
```

## Sum 1 to n

**Recursive:**
```python
def sum_to_n(n):
    if n == 1:
        return 1
    return n + sum_to_n(n - 1)
```

**Iterative:**
```python
def sum_to_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total
```

## Fibonacci

**Recursive:**
```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
```

**Iterative:**
```python
def fibonacci(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
```

## Comparison

| Aspect | Recursion | Iteration |
|--------|-----------|-----------|
| Code | Often shorter | Often longer |
| Memory | Uses call stack | Constant |
| Speed | Function call overhead | Usually faster |
| Risk | Stack overflow | None |

## When to Use Recursion

✅ Good for:
- Tree/graph traversal
- Divide and conquer
- Problems with natural recursive structure
- When code clarity matters more than performance

❌ Avoid when:
- Deep recursion possible (> 1000 calls)
- Performance is critical
- Simple loop works fine

## Python's Recursion Limit

```python
import sys
print(sys.getrecursionlimit())  # 1000

# This will crash:
def deep(n):
    if n == 0:
        return 0
    return 1 + deep(n - 1)

deep(10000)  # RecursionError!
```

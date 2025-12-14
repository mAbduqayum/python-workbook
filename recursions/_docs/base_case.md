# Base Case

## The Problem

Without a stopping point, recursion runs forever:

```python
def countdown(n):
    print(n)
    countdown(n - 1)  # never stops!

countdown(3)  # 3, 2, 1, 0, -1, -2, ... crash!
```

## The Solution: Base Case

Every recursive function needs:
1. **Base case** - when to stop (return without calling itself)
2. **Recursive case** - when to continue (call itself)

```python
def countdown(n):
    if n <= 0:          # base case
        print("Done!")
        return
    print(n)
    countdown(n - 1)    # recursive case

countdown(3)
# 3
# 2
# 1
# Done!
```

## Fixed Examples

### Factorial

```python
def factorial(n):
    if n <= 1:          # base case: 0! = 1, 1! = 1
        return 1
    return n * factorial(n - 1)
```

### Sum 1 to n

```python
def sum_to_n(n):
    if n == 1:          # base case
        return 1
    return n + sum_to_n(n - 1)
```

### Fibonacci

```python
def fibonacci(n):
    if n == 0:          # base case 1
        return 0
    if n == 1:          # base case 2
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
```

## Rules

1. Base case must be reachable
2. Each recursive call must move toward base case
3. Base case returns a value (doesn't call itself)

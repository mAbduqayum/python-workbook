# Memoization

## The Problem

Naive Fibonacci is very slow:

```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(40))  # try this - takes many seconds!
```

Why? It recalculates the same values many times:

```
fib(5)
├── fib(4)
│   ├── fib(3)
│   │   ├── fib(2)
│   │   └── fib(1)
│   └── fib(2)
└── fib(3)          ← calculated again!
    ├── fib(2)
    └── fib(1)
```

`fib(3)` is calculated 2 times, `fib(2)` is calculated 3 times...

For `fib(40)`, that adds up to more than 300 million calls!

## The Solution: Memoization

Store results to avoid recalculation:

```python
memo = {}

def fibonacci(n):
    if n in memo:
        return memo[n]

    if n <= 1:
        result = n
    else:
        result = fibonacci(n - 1) + fibonacci(n - 2)

    memo[n] = result
    return result

print(fibonacci(40))   # instant!
print(fibonacci(100))  # still instant!
```

## How It Works

1. Before calculating, check if we already have the answer
2. If yes, return it immediately
3. If no, calculate it and store for later

```
memo = {}
First call: fib(5) → calculate, store memo[5] = 5
├── fib(4) → calculate, store memo[4] = 3
│   ├── fib(3) → calculate, store memo[3] = 2
│   │   ├── fib(2) → calculate, store memo[2] = 1
│   │   │   ├── fib(1) → base case, store memo[1] = 1
│   │   │   └── fib(0) → base case, store memo[0] = 0
│   │   └── fib(1) → found in memo! return 1
│   └── fib(2) → found in memo! return 1
└── fib(3) → found in memo! return 2

memo = {1: 1, 0: 0, 2: 1, 3: 2, 4: 3, 5: 5}
```

Each value is stored only after the calls inside it return, so `fib(5)`, the first call, is
the last one stored.

## Another Example: Climbing Stairs

**Question:** How many ways to climb n stairs (1 or 2 steps at a time)?

Without memoization (slow):
```python
def climb_stairs(n):
    if n <= 2:
        return n
    return climb_stairs(n - 1) + climb_stairs(n - 2)
```

With memoization (fast):
```python
memo = {}

def climb_stairs(n):
    if n in memo:
        return memo[n]

    if n <= 2:
        result = n
    else:
        result = climb_stairs(n - 1) + climb_stairs(n - 2)

    memo[n] = result
    return result

print(climb_stairs(50))  # instant!
```

## When to Use Memoization

Use when:
- Same inputs are calculated multiple times
- Function always returns same result for same input
- You see patterns like `f(n-1) + f(n-2)`

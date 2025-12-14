# What is Recursion?

## Math Definition

In mathematics, recursion defines something in terms of itself.

### Example: Factorial

```
5! = 5 × 4 × 3 × 2 × 1 = 120
```

But we can also write:
```
5! = 5 × 4!
4! = 4 × 3!
3! = 3 × 2!
2! = 2 × 1!
1! = 1
```

So: `n! = n × (n-1)!`

### Example: Fibonacci

```
F(0) = 0
F(1) = 1
F(n) = F(n-1) + F(n-2)
```

Sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...

### Example: Sum 1 to n

```
sum(1) = 1
sum(2) = 2 + 1 = 3
sum(3) = 3 + 2 + 1 = 6
sum(n) = n + sum(n-1)
```

## In Programming

A function that calls itself:

```python
def factorial(n):
    return n * factorial(n - 1)
```

But wait... this has a problem! When does it stop?

```
factorial(3)
= 3 * factorial(2)
= 3 * 2 * factorial(1)
= 3 * 2 * 1 * factorial(0)
= 3 * 2 * 1 * 0 * factorial(-1)
= ... forever!
```

We need a **stopping condition** - see next lesson.

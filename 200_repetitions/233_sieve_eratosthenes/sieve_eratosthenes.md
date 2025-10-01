# Sieve of Eratosthenes

Find all prime numbers up to a given limit using the Sieve of Eratosthenes algorithm.

## Task
- Read a positive integer `n` from the user
- Find all prime numbers from 2 to `n` using the Sieve of Eratosthenes
- Display all prime numbers, one per line
- If `n` < 2, display an error message

## Algorithm
1. Create a list of boolean values from 0 to n (all True initially)
2. Mark 0 and 1 as not prime (False)
3. Starting from 2:
   - If current number is marked as prime:
     - It is a prime number
     - Mark all its multiples as not prime
4. Continue until you reach √n
5. Display all numbers still marked as prime

## Examples
**Example 1:**
```
20
```
```
2
3
5
7
11
13
17
19
```

**Example 2:**
```
10
```
```
2
3
5
7
```

**Example 3:**
```
1
```
```
Error: n must be at least 2
```

## Logic
- Create a list: `is_prime = [True] * (n + 1)`
- Mark `is_prime[0] = False` and `is_prime[1] = False`
- For each number i from 2 to √n:
  - If `is_prime[i]` is True:
    - Mark all multiples of i as False
    - Start from i*i (earlier multiples already marked)
- Display all numbers where `is_prime[number]` is True

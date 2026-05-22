# Sieve of Eratosthenes

Create a function to find all prime numbers up to a given number (inclusive) using the Sieve of Eratosthenes algorithm.

## Template:

```python
def sieve_of_eratosthenes(n: int) -> list[int]:
    pass


if __name__ == "__main__":
    # Test your function
    print(sieve_of_eratosthenes(20))  # [2, 3, 5, 7, 11, 13, 17, 19]
    print(sieve_of_eratosthenes(10))  # [2, 3, 5, 7]
```

## Algorithm

1. Make a boolean list `is_prime` of length `n + 1`, all `True`, then mark `0` and `1` as `False`.
2. For each `i` from `2` up to `√n`, if `is_prime[i]` is still `True`, mark every multiple of `i` starting at `i²` (`i²`, `i² + i`, `i² + 2i`, …) as `False`.
3. The primes are the indices still marked `True`.

<details>
<summary><strong>Historical Note</strong></summary>

Eratosthenes of Cyrene (c. 276–194 BCE) developed this efficient prime-finding algorithm in the 3rd century BCE. His genius extended far beyond mathematics—he calculated the Earth's circumference with remarkable accuracy, determined the tilt of Earth's axis, and served as Chief Librarian at the legendary Library of Alexandria, one of the most prestigious scholarly positions in the ancient world.

</details>

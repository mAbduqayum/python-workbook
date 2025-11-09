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

<details>
<summary><strong>Hint</strong></summary>

- Create a boolean list `primes` of size n+1, initialized to True
- Set primes[0] and primes[1] to False (0 and 1 are not prime)
- For each number i from 2 to √n:
    - If primes[i] is True:
        - Mark all multiples of i (i², i²+i, i²+2i, ...) as False
- Collect all indices where primes is True

</details>

## Note

- This is an efficient algorithm for finding all primes up to n
- Time complexity: `O(n log log n)`
- More efficient than checking each number individually

<details>
<summary><strong>Historical Note</strong></summary>

Eratosthenes of Cyrene (c. 276–194 BCE) developed this efficient prime-finding algorithm in the 3rd century BCE. His genius extended far beyond mathematics—he calculated the Earth's circumference with remarkable accuracy, determined the tilt of Earth's axis, and served as Chief Librarian at the legendary Library of Alexandria, one of the most prestigious scholarly positions in the ancient world.

</details>

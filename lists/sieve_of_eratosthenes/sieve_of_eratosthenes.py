def sieve_of_eratosthenes(n: int) -> list[int]:
    if n < 2:
        return []

    primes = [True] * (n + 1)
    primes[0] = primes[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False

    return [i for i in range(n + 1) if primes[i]]


if __name__ == "__main__":
    # Test your function
    print(sieve_of_eratosthenes(20))  # [2, 3, 5, 7, 11, 13, 17, 19]
    print(sieve_of_eratosthenes(10))  # [2, 3, 5, 7]

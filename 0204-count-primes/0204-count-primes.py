class Solution:
    def countPrimes(self, n: int) -> int:
        if n<=1:
            return 0
        is_prime = [True] * n  # initialize all numbers as prime
        is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime
        count = 0  # to count the number of primes

        for i in range(2, n):
            if is_prime[i]:
                count += 1  # found a prime number
                # mark all multiples of i as composite
                for j in range(i*i, n, i):
                    is_prime[j] = False

        return count
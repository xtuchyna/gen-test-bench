import unittest
from itertools import count, islice

def prime_generator():
    yield 2
    yield 3
    yield 5
    primes = [2, 3, 5]
    for n in count(7, 2):  # Open-ended counter starts at 7, increments by 2
        is_prime = True
        for p in primes:
            if p * p > n:
                break
            if n % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(n)
            yield n


class TestPrimeGenerator(unittest.TestCase):

    def test_first_twenty_primes(self):
        expected = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
        actual = list(islice(prime_generator(), 20))
        self.assertEqual(actual, expected)

    def test_primes_between_100_and_150(self):
        expected = [101, 103, 107, 109, 113, 127, 131, 137, 139, 149]
        gen = prime_generator()
        actual = [p for p in gen if 100 < p < 150]
        self.assertEqual(actual, expected)


    def test_number_of_primes_between_7700_and_8000(self):
        gen = prime_generator()
        count = 0
        for p in gen:
            if 7700 < p < 8000:
                count += 1
            elif p >= 8000:
                break
        self.assertEqual(count, 16)

    def test_10000th_prime(self):
        expected = 104729
        actual = list(islice(prime_generator(), 10000))[-1]
        self.assertEqual(actual, expected)


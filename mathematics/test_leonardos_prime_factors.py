import leonardos_prime_factors
import math

# Path: Mathematics\test_leonardo's_prime_factors.py

def test_wilsons_theorem():
    wilsons_theorem = leonardos_prime_factors.wilsons_theorem
    assert wilsons_theorem(2) == True
    assert wilsons_theorem(3) == True
    assert wilsons_theorem(4) == False
    assert wilsons_theorem(5) == True
    assert wilsons_theorem(6) == False
    assert wilsons_theorem(7) == True
    assert wilsons_theorem(8) == False
    assert wilsons_theorem(9) == False
    assert wilsons_theorem(10) == False

def test_generate_primes():
    assert leonardos_prime_factors.generate_primes(24) == [1, 2, 3, 5, 7, 11, 13, 17, 19, 23]

def test_all_multiples_less_than_n():
    assert leonardos_prime_factors.all_multiples_less_than_n(2, 10) == [2, 4, 6, 8]

def test_eratosthenes_sieve():
    assert leonardos_prime_factors.eratosthenes_sieve(24) == [2, 3, 5, 7, 11, 13, 17, 19, 23]

def test_generate_n_primes():
    assert leonardos_prime_factors.generate_n_primes(10) == [1, 2, 3, 5, 7, 11, 13, 17, 19, 23]
    assert leonardos_prime_factors.generate_n_primes(9) == [1, 2, 3, 5, 7, 11, 13, 17, 19]
    assert leonardos_prime_factors.generate_n_primes(8) == [1, 2, 3, 5, 7, 11, 13, 17]
    assert leonardos_prime_factors.generate_n_primes(7) == [1, 2, 3, 5, 7, 11, 13]
    assert leonardos_prime_factors.generate_n_primes(6) == [1, 2, 3, 5, 7, 11]
    assert leonardos_prime_factors.generate_n_primes(5) == [1, 2, 3, 5, 7]
    assert leonardos_prime_factors.generate_n_primes(4) == [1, 2, 3, 5]
    assert leonardos_prime_factors.generate_n_primes(3) == [1, 2, 3]
    assert leonardos_prime_factors.generate_n_primes(2) == [1, 2]
    assert leonardos_prime_factors.generate_n_primes(1) == [1]
    
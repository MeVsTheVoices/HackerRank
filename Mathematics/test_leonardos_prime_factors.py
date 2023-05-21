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
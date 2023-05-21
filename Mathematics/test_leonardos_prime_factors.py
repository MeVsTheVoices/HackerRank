import leonardos_prime_factors
import math

# Path: Mathematics\test_leonardo's_prime_factors.py

def test_wilsons_theorem_1():
    for i in range(1, 100):
        possible_prime = (leonardos_prime_factors.wilsons_theorem(i))
        print(possible_prime)
        for j in range (1, math.floor(math.sqrt(possible_prime))):
            assert possible_prime%j != 0
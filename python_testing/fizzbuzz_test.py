# Input: n = 3
# Output: ["1","2","Fizz"]

import unittest
# cs497\assignment4\findkclosestelements\solution.py
from cs497.final.fizzbuzz import Solution

class TestSolution(unittest.TestCase):
    def testFizzBuzz(self):
        s = Solution()
        self.assertEqual(s.fizzBuzz(3), ["1","2","Fizz"])
        self.assertEqual(s.fizzBuzz(5), ["1","2","Fizz","4","Buzz"])
        self.assertEqual(s.fizzBuzz(15), ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"])
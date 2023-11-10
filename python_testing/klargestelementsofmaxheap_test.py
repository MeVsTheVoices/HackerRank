import unittest
from cs497.assignment4.klargestelementofmaxheap.solution import Solution

class TestSolution(unittest.TestCase):
    def testFindKthLargest(self):
        input = [15, 13, 12, 10, 8, 9]
        k = 5
        expected = [15, 13, 12, 10, 9]
        actual = Solution().findKthLargest(input, k)
        self.assertEqual(expected, actual)
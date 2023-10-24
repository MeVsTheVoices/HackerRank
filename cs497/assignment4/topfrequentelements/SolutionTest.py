import unittest
import Solution

class SolutionTest(unittest.TestCase):
    def testTopKFrequent():
        # Input: nums = [1,1,1,2,2,3], k = 2
        # Output: [1,2]
        self.assertEqual(Solution.topKFrequent([1,1,1,2,2,3], 2), [1,2])
        # Input: nums = [1], k = 1
        # Output: [1]
        self.assertEqual(Solution.topKFrequent([1], 1), [1])
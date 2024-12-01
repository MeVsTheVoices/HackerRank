import unittest
from leetcode.islandperimeter.solution import Solution

class TestSolution(unittest.TestCase):
    def testIslandPerimeter(self):
        sol = Solution()
        self.assertEqual(sol.islandPerimeter([[0,1,0,0],
                                             [1,1,1,0],
                                             [0,1,0,0],
                                             [1,1,0,0]]), 16)

        
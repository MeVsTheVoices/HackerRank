import unittest
from cs497.assignment6.connectingcitieswithminimumcost.solution import Solution

class TestSolution(unittest.TestCase):
    def testConnectAllCities(self):
        sol = Solution()
        connections = [[1,2,5],[1,3,6],[2,3,1]]
        expected = 6
        actual = sol.connectAllCities(connections)
        self.assertEqual(expected, actual)
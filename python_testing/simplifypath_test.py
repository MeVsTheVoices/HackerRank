import unittest
from leetcode.simplifypath.solution import Node, Solution

"""
class Node:
    def __init__(self, parent = None):
        self.parent = parent
        self.children = []
        self.value = None
"""

class TestSolution(unittest.TestCase):
    def testSimplifyPath(self):
        sol = Solution()
        path = "/home/user/Documents/../Pictures"
        actual = sol.simplifyPath(path)
        expected = "/home/user/Pictures"
        self.assertEqual(actual, expected)
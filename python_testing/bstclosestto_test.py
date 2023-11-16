import unittest

from cs497.interviewNOV16.solution import Solution
from cs497.assignment5.treeNode import TreeNode

class SolutionTest(unittest.TestCase):
    def testMaxDiff(self):
        root = TreeNode(4)
        root.left = TreeNode(2)
        root.right = TreeNode(5)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(3)

        solution = Solution()
        self.assertEqual(4, solution.maxDiff(root, 3.714286))
        

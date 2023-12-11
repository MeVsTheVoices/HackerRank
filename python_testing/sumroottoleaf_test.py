import unittest

from cs497.interviewNOV28.solution import Solution
from cs497.interviewNOV28.solution import TreeNode

class TestSolution(unittest.TestCase):
    def testSumRootToLeaf(self):
        root = TreeNode(1)
        root.left = TreeNode(0)
        root.right = TreeNode(1)
        root.left.left = TreeNode(0)
        root.left.right = TreeNode(1)
        root.right.left = TreeNode(0)
        root.right.right = TreeNode(1)

        solution = Solution()
        self.assertEqual(solution.sumRootToLeaf(root), 22)
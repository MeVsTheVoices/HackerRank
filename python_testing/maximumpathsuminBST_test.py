import unittest
from cs497.assignment5.maximumpathsuminBST.solution import Solution
from cs497.assignment5.treeNode import TreeNode

class TestSolution(unittest.TestCase):
    def testMaxPathSum(self):
        sol = Solution()
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        expected = 6
        actual = sol.maxPathSum(root)
        self.assertEqual(expected, actual)

        root = TreeNode(-10)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        expected = 42
        actual = sol.maxPathSum(root)
        self.assertEqual(expected, actual)
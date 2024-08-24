import unittest
from leetcode.preorder.solution import Solution
from cs497.assignment5.treeNode import TreeNode

class TestSolution(unittest.TestCase):
    def testPreorderTraversal(self):
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.left = TreeNode(3)
        s = Solution()
        self.assertEqual(s.preorderTraversal(root), [1, 2, 3])
import unittest
from cs497.assignment5.treeNode import TreeNode
from leetcode.invertbinarytree.solution import Solution

class TestSolution(unittest.TestCase):
    def testInvertTree(self):
        sol = Solution()
        tree = TreeNode(4)
        tree.left = TreeNode(2)
        tree.right = TreeNode(7)
        tree.left.left = TreeNode(1)
        tree.left.right = TreeNode(3)
        tree.right.left = TreeNode(6)
        tree.right.right = TreeNode(9)
        inverted = sol.invertTree(tree)
        self.assertEqual(inverted.val, 4)
        self.assertEqual(inverted.left.val, 7)
        self.assertEqual(inverted.right.val, 2)
        self.assertEqual(inverted.left.left.val, 9)
        self.assertEqual(inverted.left.right.val, 6)
        self.assertEqual(inverted.right.left.val, 3)
        self.assertEqual(inverted.right.right.val, 1)

        
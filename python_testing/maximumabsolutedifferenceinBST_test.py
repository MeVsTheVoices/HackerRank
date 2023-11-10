import unittest
from cs497.assignment5.maximumabsolutedifferenceinBST.solution import Solution
from cs497.assignment5.treeNode import TreeNode

class TestSolution(unittest.TestCase):
    def testGetMaximumDifference(self):
        sol = Solution()
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        result = sol.getMaximumDifference(root)
        self.assertEqual(result, 2)

        root = TreeNode(1)
        root.left = TreeNode(0)
        root.right = TreeNode(48)
        root.right.left = TreeNode(12)
        root.right.right = TreeNode(49)
        result = sol.getMaximumDifference(root)
        self.assertEqual(result, 49)
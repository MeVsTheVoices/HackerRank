import unittest
from cs497.final.longestconsecutivesequence import Solution
from cs497.final.treeNode import TreeNode

class TestSolution(unittest.TestCase):
    def testLongestConsecutiveSequence(self):
        # Input: root = [1,null,3,2,4,null,null,null,5]
        # Output: 3
        # Input: root = [2,null,3,2,null,1]
        # Output: 2
        solution = Solution()
        self.assertEqual(solution.longestConsecutiveSequence(None), 0)
        root = TreeNode(1)
        root.right = TreeNode(3)
        root.right.left = TreeNode(2)
        root.right.right = TreeNode(4)
        root.right.right.right = TreeNode(5)
        self.assertEqual(solution.longestConsecutiveSequence(root), 3)

        root = TreeNode(2)
        root.right = TreeNode(3)
        root.right.left = TreeNode(2)
        root.right.left.left = TreeNode(1)
        self.assertEqual(solution.longestConsecutiveSequence(root), 2)
        



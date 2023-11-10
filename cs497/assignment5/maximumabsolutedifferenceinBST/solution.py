from typing import Optional, Final
import sys
from cs497.assignment5.treeNode import TreeNode

class Solution:
    def getMaximumDifference(self, root: Optional[TreeNode]) -> int:
        greatestSoFar = (-sys.maxsize) - 1
        leastSoFar = sys.maxsize

        def traverse(node):
            nonlocal greatestSoFar, leastSoFar
            if node is None:
                return
            if node.val > greatestSoFar:
                greatestSoFar = node.val
            if node.val < leastSoFar:
                leastSoFar = node.val
            traverse(node.left)
            traverse(node.right)

            return greatestSoFar, leastSoFar

        greatestSoFar, leastSoFar = traverse(root)
        return greatestSoFar - leastSoFar

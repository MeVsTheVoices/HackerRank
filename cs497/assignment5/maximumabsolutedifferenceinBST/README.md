# Testing
Testing is in python_testing\maximumabsolutedifferenceinBST_test.py

# Intuition
We only need to find the greatest and least values in the tree, then return the difference between them.

# Approach
    - First, find the greatest and least values in the tree
    - Then, return the difference between them


# Complexity
- Time complexity: O(log(n))
    - We have to traverse the tree once to find the greatest and least values
- Space complexity: O(1)

# Code
```
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
```
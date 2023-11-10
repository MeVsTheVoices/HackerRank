from math import inf
from typing import Optional
from cs497.assignment5.treeNode import TreeNode


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            # We're returning two variables, the first denotes the greatest value of the roots children
            # we can get without splitting, the second is the greatest path sum found so far
            if not root:
                return -inf, -inf
            leftWithoutSplit, maxInLeft = dfs(root.left)
            rightWithoutSplit, maxInRight = dfs(root.right)
            # If we split, then we can only traverse one subtree including the current node
            maxWithoutSplit = root.val + max(0, leftWithoutSplit, rightWithoutSplit)
            # We return this, along with the greatest path sum we've found so far
            # for this we have four considerations, the greatest sum without splitting
            # those of the left and right subtrees, and the path sum were
            # we to split to both left and right subtrees
            maxWithSplit = root.val + leftWithoutSplit + rightWithoutSplit
            return maxWithoutSplit, max(maxWithoutSplit, maxInLeft, maxInRight, maxWithSplit)
        return dfs(root)[1]

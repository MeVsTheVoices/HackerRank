from typing import List

from cs497.final.treeNode import TreeNode


class Solution:
    def longestConsecutiveSequence(self, node: TreeNode) -> int:
        if node is None:
            return 0
        return self.dfs(node, 1)
    
    def dfs(self, node: TreeNode, length: int) -> int:
        if node.left is None and node.right is None:
            return length
        leftLength = 0
        rightLength = 0
        if node.left is not None:
            if node.left.val == node.val + 1:
                leftLength = self.dfs(node.left, length + 1)
            else:
                leftLength = self.dfs(node.left, 1)
        if node.right is not None:
            if node.right.val == node.val + 1:
                rightLength = self.dfs(node.right, length + 1)
            else:
                rightLength = self.dfs(node.right, 1)
        return max(length, leftLength, rightLength)
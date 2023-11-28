# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        from typing import Optional


class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        total = 0
        stack = [(root,str(root.val))]

        while stack:
            node, value = stack.pop()

            if node.left:
                stack.append((node.left, value + str(node.left.val)))

            if node.right:
                stack.append((node.right, value + str(node.right.val)))

            if not node.left and not node.right:
                total += int(value, 2)

        return total
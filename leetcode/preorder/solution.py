from cs497.assignment5.treeNode import TreeNode
from typing import List, Optional

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        order = []
        def preorderHelper(node):
            if node:
                order.append(node.val)
            else:
                return
            if node.left:
                preorderHelper(node.left)
            if node.right:
                preorderHelper(node.right)
        preorderHelper(root)
        return order
                
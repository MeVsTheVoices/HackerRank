from typing import Optional

from cs497.assignment5.treeNode import TreeNode

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        def invertTreeRecursive(node):
            if not node:
                return
            temp = node.left
            node.left = node.right
            node.right = temp

            invertTreeRecursive(node.left)
            invertTreeRecursive(node.right)
        
        invertTreeRecursive(root)

        return root
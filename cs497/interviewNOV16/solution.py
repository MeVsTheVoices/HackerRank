from cs497.assignment5.treeNode import TreeNode

class Solution:
    def maxDiff(self, root: TreeNode, target: float) -> int:
        closestTo = root.val

        def traverse(node: TreeNode):
            nonlocal closestTo
            if not node:
                return
            
            if (abs(node.val - target)) < (abs(closestTo - target)):
                closestTo = node.val

            traverse(node.left)
            traverse(node.right)

        traverse(root)
        return closestTo

        
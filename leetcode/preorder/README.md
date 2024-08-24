# Intuition
Preorder, inorder, and postorder just require us to change the sequence of three operations.

# Approach
Preorder takes root, then left, then right. Python has closures, so that makes life easy as where to append values.

# Complexity
- Time complexity: O(log(n))

- Space complexity: O(n)

# Code
```python3 []
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
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
                
```
# Intuition
Just flip em

# Approach
No need for a new tree, though that would work, just traverse and swap right and left nodes

# Complexity
- Time complexity: O(log(n))

- Space complexity: O(1)

# Code
```python3 []
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
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
```
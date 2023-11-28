# Testing
Testing is at python_testing/sumroottoleaf_test.py

# Intuition
We do a DFS and append to strings.

# Approach
    - DFS
    - Append to strings
    - Convert to int

# Complexity
- Time complexity: $$O(log(n))$$

- Space complexity: O(n)

# Code
```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
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
```
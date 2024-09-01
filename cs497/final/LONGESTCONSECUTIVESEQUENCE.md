# Intuition
DFS is back. We're only including the left or right subtree in our return value if that node has a value consecutive to the current node. Otherwise, we're resetting the length to 1.


# Approach
1. If the node is None, return 0
2. Call dfs on the node with a length of 1
3. If the node is a leaf, return the length
4. If the node has a left child, call dfs on the left child with a length of length + 1 if the left child's value is consecutive to the current node's value, otherwise call dfs on the left child with a length of 1


# Complexity
- Time complexity: O(log(n))
  - At each substep, we're cutting the number of nodes we need to examine in half, so O(log(n))

- Space complexity: O(n)
    - In the worst possible case, we can imagine a tree of only consecutive numbers that are all left children

# Code
```
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
```
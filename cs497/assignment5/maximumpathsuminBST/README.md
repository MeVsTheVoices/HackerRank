# Intuition
I wanted to avoid using a global variable. We've written this before for another assignment, now I'm just doing
it in python for practice. I'm using a tuple to return two values from the dfs function. The first value is the
maximum path sum that doesn't include the current node. The second value is the maximum path sum that includes
the current node. The maximum path sum that includes the current node is the maximum of the maximum path sum
that doesn't include the current node, the maximum path sum in the left subtree, the maximum path sum in the
right subtree, and the maximum path sum that includes the current node. The maximum path sum that doesn't include
the current node is the maximum of the current node's value, the maximum path sum that doesn't include the left
subtree, and the maximum path sum that doesn't include the right subtree. The base case is when the current node
is None. In this case, the maximum path sum that doesn't include the current node is negative infinity and the
maximum path sum that includes the current node is negative infinity. The answer is the maximum path sum that
includes the root node.

# Approach
To avoid keeping a global variable, the current greatest path sum is kept as the second value in the tuple.

# Complexity
- Time complexity: O(log(n))
    - The time complexity is O(log(n)) because the dfs function is called on each node in the tree.

- Space complexity: O(1)
    - As compared to BFS, DFS uses less memory because it doesn't need to store all the nodes in the queue.

# Code
```
from math import inf
from typing import Optional


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return -inf, -inf
            leftWithoutSplit, maxInLeft = dfs(root.left)
            rightWithoutSplit, maxInRight = dfs(root.right)

            maxWithoutSplit = root.val + max(0, leftWithoutSplit, rightWithoutSplit)

            maxWithSplit = root.val + leftWithoutSplit + rightWithoutSplit
            return maxWithoutSplit, max(maxWithoutSplit, maxInLeft, maxInRight, maxWithSplit)
        return dfs(root)[1]

```
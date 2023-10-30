# Intuition
We're solving the sum of left leaves. We can do this recursively by checking if the left node is a leaf node. If it is, we add it to the sum. We then recursively call the function on the left and right nodes.

# Approach
- Check if the root is null. If it is, return 0.
- Check if the left node is a leaf node. If it is, add it to the sum.
- Recursively call the function on the left and right nodes.
- Return the sum.

# Complexity
- Time complexity: O(log(n))

- Space complexity: O(1)

# Code
```

class Solution {
    public int sumOfLeftLeaves(TreeNode root) {
        return sumOfLeftTreeLeavesHelper(root);
    }

    public int sumOfLeftTreeLeavesHelper(TreeNode root) {
        if (root == null)
            return 0;
        int sum = 0;
        if (root.left != null && root.left.left == null && root.left.right == null)
            sum += root.left.val;

        sum += sumOfLeftTreeLeavesHelper(root.left);
        sum += sumOfLeftTreeLeavesHelper(root.right);

        return sum;
    }
}
```
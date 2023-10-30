package cs497.quiz5;

import cs497.quiz5.TreeNode;

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
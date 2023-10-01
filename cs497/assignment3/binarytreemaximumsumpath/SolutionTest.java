package cs497.assignment3.binarytreemaximumsumpath;

import static org.junit.Assert.assertEquals;

import org.junit.Test;

import cs497.assignment3.TreeNode;

public class SolutionTest {
    @Test
    public void testMaxPathSum() {
        // Test case [5,4,8,11,null,13,4,7,2,null,null,null,1]
        // Expected output: 48
        TreeNode root = new TreeNode(5);
        TreeNode left = new TreeNode(4);
        TreeNode right = new TreeNode(8);
        root.left = left;
        root.right = right;
        TreeNode leftLeft = new TreeNode(11);
        left.left = leftLeft;
        TreeNode rightLeft = new TreeNode(13);
        TreeNode rightRight = new TreeNode(4);
        right.left = rightLeft;
        right.right = rightRight;
        TreeNode leftLeftLeft = new TreeNode(7);
        TreeNode leftLeftRight = new TreeNode(2);
        leftLeft.left = leftLeftLeft;
        leftLeft.right = leftLeftRight;
        TreeNode rightRightRight = new TreeNode(1);
        rightRight.right = rightRightRight;
        Solution solution = new Solution();
        int result = solution.maxPathSum(root);
        assertEquals(48, result);

        // Test case [1,2,3]
        // Expected output: 6
        root = new TreeNode(1);
        left = new TreeNode(2);
        right = new TreeNode(3);
        root.left = left;
        root.right = right;
        solution = new Solution();
        result = solution.maxPathSum(root);
        assertEquals(6, result);

        // Test case [-10,9,20,null,null,15,7]
        // Expected output: 42
        root = new TreeNode(-10);
        left = new TreeNode(9);
        right = new TreeNode(20);
        root.left = left;
        root.right = right;
        rightLeft = new TreeNode(15);
        rightRight = new TreeNode(7);
        right.left = rightLeft;
        right.right = rightRight;
        solution = new Solution();
        result = solution.maxPathSum(root);
        assertEquals(42, result);
    }
}

package cs497.quiz6;

import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class SolutionTest {
    @Test
    public void testIncreasingBST() {
        TreeNode root = new TreeNode(5);
        root.left = new TreeNode(3);
        root.right = new TreeNode(6);
        TreeNode left = root.left;
        left.left = new TreeNode(2);
        left.right = new TreeNode(4);
        TreeNode right = root.right;
        right.right = new TreeNode(8);
        right.right.left = new TreeNode(7);
        right.right.right = new TreeNode(9);

        TreeNode expected = new TreeNode(2);
        expected.right = new TreeNode(3);
        expected.right.right = new TreeNode(4);
        expected.right.right.right = new TreeNode(5);
        expected.right.right.right.right = new TreeNode(6);
        expected.right.right.right.right.right = new TreeNode(7);
        expected.right.right.right.right.right.right = new TreeNode(8);
        expected.right.right.right.right.right.right.right = new TreeNode(9);

        Solution solution = new Solution();
        TreeNode actual = solution.increasingBST(root);

        assertEquals(expected.val, actual.val);
        assertEquals(expected.right.val, actual.right.val);
        assertEquals(expected.right.right.val, actual.right.right.val);
        assertEquals(expected.right.right.right.val, actual.right.right.right.val);
        assertEquals(expected.right.right.right.right.val, actual.right.right.right.right.val);
        assertEquals(expected.right.right.right.right.right.val, actual.right.right.right.right.right.val);
        assertEquals(expected.right.right.right.right.right.right.val, actual.right.right.right.right.right.right.val);
        assertEquals(expected.right.right.right.right.right.right.right.val, actual.right.right.right.right.right.right.right.val);    
    }
}
package cs497.assignment3.buildtreefrominandpreorder;

import static org.junit.Assert.assertEquals;

import org.junit.Test;

import cs497.assignment3.TreeNode;

public class SolutionTest {
    @Test
    public void testBuildTree() {
        Solution s = new Solution();
        int[] preorder = {1, 2, 4, 5, 3, 6, 7};
        int[] inorder = {4, 2, 5, 1, 6, 3, 7};
        TreeNode root = s.buildTree(preorder, inorder);
        assertEquals(1, root.val);
        assertEquals(2, root.left.val);
        assertEquals(3, root.right.val);
        assertEquals(4, root.left.left.val);
        assertEquals(5, root.left.right.val);
        assertEquals(6, root.right.left.val);
        assertEquals(7, root.right.right.val);
    }
}
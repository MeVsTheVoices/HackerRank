package cs497.assignment3.balancebinarytree;

import static org.junit.Assert.assertArrayEquals;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import org.junit.Test;

import cs497.assignment3.TreeNode;

public class SolutionTest {
    @Test
    public void testInorderTraversal() {
        TreeNode r1 = new TreeNode(1);
        r1.left = new TreeNode(2);
        r1.right = new TreeNode(3);
        r1.left.left = new TreeNode(4);
        r1.left.right = new TreeNode(5);
        ArrayList<Integer> expected = new ArrayList<Integer>();
        expected.addAll(Arrays.asList(4, 2, 5, 1, 3));

        Solution s = new Solution();
        List<Integer> list = s.inOrderTraversal(r1);
        assertArrayEquals(expected.toArray(), list.toArray());
    }

    @Test
    public void testRecreateBST() {
        ArrayList<Integer> list = new ArrayList<Integer>();
        list.addAll(Arrays.asList(1, 2, 3, 4, 5));
        Solution s = new Solution();
        TreeNode root = s.recreateBST(list, 0, list.size() - 1);
        List<Integer> list2 = s.inOrderTraversal(root);
        assertArrayEquals(list.toArray(), list2.toArray());
    }

    @Test
    public void testBalanceBST() {
        TreeNode r1 = new TreeNode(1);
        r1.right = new TreeNode(2);
        r1.right.right = new TreeNode(3);
        r1.right.right.right = new TreeNode(4);
        r1.right.right.right.right = new TreeNode(5);
        ArrayList<Integer> expected = new ArrayList<Integer>();
        expected.addAll(Arrays.asList(1, 2, 3, 4, 5));

        Solution s = new Solution();
        TreeNode r = s.balanceBST(r1);
        List<Integer> list = s.inOrderTraversal(r);
        assertArrayEquals(expected.toArray(), list.toArray());
    }
}

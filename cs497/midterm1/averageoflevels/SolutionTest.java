package cs497.midterm1.averageoflevels;

import static org.junit.Assert.assertEquals;

import java.util.List;

import org.junit.Test;

import cs497.midterm1.TreeNode;

public class SolutionTest {
    @Test
    public void testAverageOfLevels() {
        TreeNode root = new TreeNode(3);
        root.left = new TreeNode(9);
        root.right = new TreeNode(20);
        root.right.right = new TreeNode(7);
        root.right.left = new TreeNode(15);
        double[] expected = {3.0, 14.5, 11.0};
        Solution solution = new Solution();
        List<Double> actual = solution.averageOfLevels(root);
        assertEquals(expected.length, actual.size());
        for (int i = 0; i < expected.length; i++) {
            assertEquals(expected[i], actual.get(i), 0.00001);
        }
    }
}

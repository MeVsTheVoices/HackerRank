package leetcode.sortanarray;

import static org.junit.Assert.assertArrayEquals;

import org.junit.Test;

public class SolutionTest {
    @Test
    public void testSortArray() {
        int[] nums = {5, 2, 3, 1};
        int[] expected = {1, 2, 3, 5};
        Solution solution = new Solution();
        int[] actual = solution.sortArray(nums);
        assertArrayEquals(expected, actual);
    }
}

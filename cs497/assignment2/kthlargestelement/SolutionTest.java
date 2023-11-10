package cs497.assignment2.kthlargestelement;

import static org.junit.Assert.assertEquals;

import org.junit.Test;

public class SolutionTest {
    @Test
    public void testfindKthLargest() {
        Solution solution = new Solution();

        int[] nums = { 3, 2, 1, 5, 6, 4 };
        int k = 2;
        int result = solution.findKthLargest(nums, k);
        assertEquals(5, result);

        nums = new int[] { 3, 2, 3, 1, 2, 4, 5, 5, 6 };
        k = 4;
        result = solution.findKthLargest(nums, k);
        assertEquals(4, result);
    }
}

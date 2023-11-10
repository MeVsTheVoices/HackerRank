package leetcode.binarysearch;

import static org.junit.Assert.assertEquals;

import org.junit.Test;

public class SolutionTest {
    @Test
    public void testSearch() {
        int nums[] = { -1, 0, 3, 5, 9, 12 };
        Solution solution = new Solution();
        assertEquals(4, solution.search(nums, 9));

        nums = new int[] {2, 5};
        assertEquals(0, solution.search(nums, 2));
    }
}

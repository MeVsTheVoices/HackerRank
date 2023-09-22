package cs497.assignment2.smallestsubarraywithsumk;

import static org.junit.Assert.assertEquals;

import org.junit.Test;

public class SolutionTest {
    @Test
    public void testShortestSubarray() {
        Solution s = new Solution();
        int[] nums = { 2, -1, 2 };
        int k = 3;
        int result = s.shortestSubarray(nums, k);
        assertEquals(3, result);
        System.out.println(result);

        nums = new int[] { 1 };
        k = 1;
        result = s.shortestSubarray(nums, k);
        assertEquals(1, result);
        System.out.println(result);

        nums = new int[] { 1, 2 };
        k = 4;
        result = s.shortestSubarray(nums, k);
        assertEquals(-1, result);
        System.out.println(result);

        nums = new int[] {84, -37, 32, 40, 95};
        k = 167;
        result = s.shortestSubarray(nums, k);
        assertEquals(3, result);
        System.out.println(result);
    }
}

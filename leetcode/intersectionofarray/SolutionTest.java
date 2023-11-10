package leetcode.intersectionofarray;

import static org.junit.Assert.assertTrue;

import org.junit.Test;

public class SolutionTest {
    @Test
    public void testIntersection() {
        int[] nums1 = {1, 2, 2, 1};
        int[] nums2 = {2, 2};

        Solution solution = new Solution();
        int[] result = solution.intersection(nums1, nums2);
        assert(result.length == 1);
        assert(result[0] == 2);

        nums1 = new int[]{4, 9, 5};
        nums2 = new int[]{9, 4, 9, 8, 4};

        result = solution.intersection(nums1, nums2);
        assert(result.length == 2);
        assertTrue(result[0] == 9 || result[0] == 4);
        assertTrue(result[1] == 9 || result[1] == 4);
    }
}

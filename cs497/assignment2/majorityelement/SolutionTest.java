package cs497.assignment2.majorityelement;

import org.junit.Test;

public class SolutionTest {
    @Test
    public void testMajorityElement() {
        Solution solution = new Solution();
        
        int[] nums = { 3, 2, 3 };
        assert solution.majorityElement(nums) == 3;

        nums = new int[] { 2, 2, 1, 1, 1, 2, 2 };
        assert solution.majorityElement(nums) == 2;
    }
}

package medianoftwosortedarrays;

import static org.junit.Assert.assertTrue;

import org.junit.Test;

public class SolutionTest {
    Solution solution;

    @Test
    public void testFindMedianSortedArrays() {
        solution = new Solution();
        int[] t1 = new int[] {1, 2, 2, 3, 4};
        int[] t2 = new int[] {1, 4, 4, 5, 6, 7, 7, 7};
        double a1 = 4.0;
        double s1 = solution.findMedianSortedArrays(t1, t2);
        assertTrue(s1 == a1);

        int[] t3 = new int[] {1, 3};
        int[] t4 = new int[] {2};
        double a2 = 2.0;
        double s2 = solution.findMedianSortedArrays(t3, t4);
        assertTrue(s2 == a2);

        int[] t5 = new int[] {1, 2};
        int[] t6 = new int[] {3, 4};
        double a3 = 2.5;
        double s3 = solution.findMedianSortedArrays(t5, t6);
        assertTrue(s3 == a3);
        
    }
}

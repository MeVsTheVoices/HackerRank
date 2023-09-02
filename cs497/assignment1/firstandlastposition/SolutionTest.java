package cs497.assignment1.firstandlastposition;

import static org.junit.Assert.assertTrue;


import java.util.Arrays;
import java.util.List;

import org.junit.Test;


public class SolutionTest {
    Solution solution;
    public SolutionTest() {
        solution = new Solution();
    }

    @Test
    public void testLeftBound() {
        int[] t1 = new int[] {1, 2, 2, 3, 3, 5, 6};
        int a1 = 3;
        int s1 = solution.leftBound(t1, a1, 0, t1.length - 1);
        assertTrue(s1 == 3);

        int[] t2 = new int[] {1, 2, 2, 3, 3, 5, 6};
        int a2 = 1;
        int s2 = solution.leftBound(t2, a2, 0, t2.length - 1);
        assertTrue(s2 == 0);
    }

    @Test
    public void testRightBound() {
        int[] t1 = new int[] {1, 2, 2, 3, 3, 5, 6};
        int a1 = 2;
        int s1 = solution.rightBound(t1, a1, 0, t1.length - 1);
        assertTrue(s1 == 2);


        int[] t2 = new int[] {1, 2, 2, 3, 3, 5, 6};
        int a2 = 1;
        int s2 = solution.rightBound(t2, a2, 0, t2.length - 1);
        assertTrue(s2 == 0);
    }

    @Test
    public void testSearchRange() {
        int[] t1 = new int[] {1, 2, 2, 3, 3, 5, 6};
        List<Integer> a1 = Arrays.asList(3, 4);
        int[] s1 = solution.searchRange(t1, 3);
        assertTrue(a1.contains(s1[0]));
        assertTrue(a1.contains(s1[1]));

        int[] t2 = new int[] {5, 7, 7, 8, 8, 10};
        List<Integer> a2 = Arrays.asList(3, 4);
        int[] s2 = solution.searchRange(t2, 8);
        assertTrue(a2.contains(s2[0]));
        assertTrue(a2.contains(s2[1]));

        int[] t3 = new int[] {5, 7, 7, 8, 8, 10};
        List<Integer> a3 = Arrays.asList(-1, -1);
        int[] s3 = solution.searchRange(t3, 6);
        assertTrue(a3.contains(s3[0]));
        assertTrue(a3.contains(s3[1]));

        int[] t4 = new int[] {};
        List<Integer> a4 = Arrays.asList(-1, -1);
        int[] s4 = solution.searchRange(t4, 0);
        assertTrue(a4.contains(s4[0]));
        assertTrue(a4.contains(s4[1]));
    }
}

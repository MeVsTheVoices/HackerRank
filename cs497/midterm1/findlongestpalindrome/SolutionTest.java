package cs497.midterm1.findlongestpalindrome;

import static org.junit.Assert.assertEquals;

import org.junit.Test;

public class SolutionTest {
    @Test
    public void testLongestPalindrome() {
        Solution solution = new Solution();
        String result = solution.longestPalindrome("babad");
        String expected = "bab";
        assertEquals(expected, result);
    }
    
}

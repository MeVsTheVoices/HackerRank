package leetcode.longestcommonprefix;

import static org.junit.Assert.assertEquals;

import org.junit.Test;

public class SolutionTest {
    @Test
    public void testLongestCommonPrefix() {
        Solution solution = new Solution();
        String[] strs = new String[] { "flower", "flow", "flight" };
        String longest = solution.longestCommonPrefix(strs);
        assertEquals("fl", longest);

        strs = new String[] { "dog", "racecar", "car" };
        longest = solution.longestCommonPrefix(strs);
        assertEquals("", longest);

        strs = new String[] { "a" };
        longest = solution.longestCommonPrefix(strs);
        assertEquals("a", longest);
    }
}

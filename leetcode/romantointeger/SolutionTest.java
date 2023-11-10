package leetcode.romantointeger;

import static org.junit.Assert.assertEquals;

import org.junit.Test;

public class SolutionTest {
    @Test
    public void testSearch() {
        Solution s = new Solution();
        String in = "III";
        int expected = 3;
        int actual = s.romanToInt(in);
        assertEquals(expected, actual);

        in = "LVIII";
        expected = 58;
        actual = s.romanToInt(in);
        assertEquals(expected, actual);

        in = "MCMXCIV";
        expected = 1994;
        actual = s.romanToInt(in);
        assertEquals(expected, actual);
    }
}

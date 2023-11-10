package cs497.midterm1.validanagram;

import static org.junit.Assert.assertEquals;

import org.junit.Test;

public class SolutionTest {
    @Test
    public void testIsAnagram() {
        Solution sol = new Solution();
        assertEquals(sol.isAnagram("anagram", "nagaram"), true);
        assertEquals(sol.isAnagram("rat", "car"), false);
    }
}

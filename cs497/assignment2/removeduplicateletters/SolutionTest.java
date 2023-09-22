package cs497.assignment2.removeduplicateletters;

import static org.junit.Assert.assertEquals;

import org.junit.Test;

public class SolutionTest {
    @Test
    public void testRemoveDuplicateLetters() {
        Solution solution = new Solution();
        assertEquals("abc", solution.removeDuplicateLetters("bcabc"));
        assertEquals("acdb", solution.removeDuplicateLetters("cbacdcbc"));
        assertEquals("abc", solution.removeDuplicateLetters("abc"));
        assertEquals("a", solution.removeDuplicateLetters("a"));
        assertEquals("", solution.removeDuplicateLetters(""));
        assertEquals("", solution.removeDuplicateLetters(null));
    }

    public static void main(String[] args) {
        SolutionTest test = new SolutionTest();
        test.testRemoveDuplicateLetters();
    }
}

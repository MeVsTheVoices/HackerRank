package cs497.assignment1.removenthnode;

import static org.junit.Assert.assertTrue;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import org.junit.Test;


public class SolutionTest {
    Solution solution;

    @Test
    public void testRemoveNthNode() {
        // Test case 1
        solution = new Solution();
        ListNode h1 = arrayToList(new int[] { 1, 2, 3, 4, 5 });
        int remove = 2;
        List<Integer> expected = Arrays.asList(1, 2, 3, 5);
        List<Integer> actual = listToArray(solution.removeNthFromEnd(h1, remove));
        assertTrue(expected.equals(actual));

        // Test case 2
        solution = new Solution();
        ListNode h2 = arrayToList(new int[] { 1 });
        remove = 1;
        expected = Arrays.asList();
        actual = listToArray(solution.removeNthFromEnd(h2, remove));
        assertTrue(expected.equals(actual));

        // Test case 3
        solution = new Solution();
        ListNode h3 = arrayToList(new int[] { 1, 2 });
        remove = 1;
        expected = Arrays.asList(1);
        actual = listToArray(solution.removeNthFromEnd(h3, remove));
        assertTrue(expected.equals(actual));
    }

    public ListNode arrayToList(int[] array) {
        ListNode head = new ListNode();
        ListNode current = head;
        for (int i = 0; i < array.length; i++) {
            current.val = array[i];
            if (i < array.length - 1) {
                current.next = new ListNode();
                current = current.next;
            }
        }
        return head;
    }

    public List<Integer> listToArray(ListNode head) {
        List<Integer> result = new ArrayList<Integer>();
        ListNode current = head;
        while (current != null) {
            result.add(current.val);
            current = current.next;
        }
        return result;
    }
}

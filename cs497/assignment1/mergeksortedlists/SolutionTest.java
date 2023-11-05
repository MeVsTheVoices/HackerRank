package cs497.assignment1.mergeksortedlists;

import static org.junit.Assert.assertEquals;

import org.junit.Test;

public class SolutionTest {
    Solution solution;

    @Test
    public void testMergeKLists() {
        // test 1
        ListNode[] lists = new ListNode[3];
        lists[0] = new ListNode(1, new ListNode(4, new ListNode(5)));
        lists[1] = new ListNode(1, new ListNode(3, new ListNode(4)));
        lists[2] = new ListNode(2, new ListNode(6));
        solution = new Solution();

        ListNode result = solution.mergeKLists(lists);
        
        ListNode expected = new ListNode(1, new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4, new ListNode(4, new ListNode(5, new ListNode(6))))))));
        while (result != null && expected != null) {
            assertEquals(expected.val, result.val);
            result = result.next;
            expected = expected.next;
        }

        // test 2
        lists = new ListNode[1];
        lists[0] = null;
        solution = new Solution();

        result = solution.mergeKLists(lists);

        expected = null;
        while (result != null && expected != null) {
            assertEquals(expected.val, result.val);
            result = result.next;
            expected = expected.next;
        }

        // test 3
        lists = new ListNode[2];
        lists[0] = null;
        lists[1] = null;
        solution = new Solution();

        result = solution.mergeKLists(lists);

        expected = null;

        while (result != null && expected != null) {
            assertEquals(expected.val, result.val);
            result = result.next;
            expected = expected.next;
        }
    }
}

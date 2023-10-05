package leetcode.mergetwosortedlists;

import static org.junit.Assert.assertEquals;

import org.junit.Test;

import leetcode.ListNode;

public class SolutionTest {
    @Test
    public void testMergeTwoLists() {
        ListNode list1 = new ListNode(1);
        list1.next = new ListNode(3);
        list1.next.next = new ListNode(5);
        list1.next.next.next = new ListNode(7);
        list1.next.next.next.next = new ListNode(9);
        ListNode list2 = new ListNode(2);
        list2.next = new ListNode(4);
        list2.next.next = new ListNode(6);
        list2.next.next.next = new ListNode(8);
        list2.next.next.next.next = new ListNode(10);
        Solution solution = new Solution();
        ListNode result = solution.mergeTwoLists(list1, list2);
        ListNode expected = new ListNode(1);
        expected.next = new ListNode(2);
        expected.next.next = new ListNode(3);
        expected.next.next.next = new ListNode(4);
        expected.next.next.next.next = new ListNode(5);
        expected.next.next.next.next.next = new ListNode(6);
        expected.next.next.next.next.next.next = new ListNode(7);
        expected.next.next.next.next.next.next.next = new ListNode(8);
        expected.next.next.next.next.next.next.next.next = new ListNode(9);
        expected.next.next.next.next.next.next.next.next.next = new ListNode(10);

        while (result != null && expected != null) {
            assertEquals(result.val, expected.val);
            result = result.next;
            expected = expected.next;
        }
    }
}
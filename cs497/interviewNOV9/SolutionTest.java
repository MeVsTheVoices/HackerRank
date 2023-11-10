package cs497.interviewNOV9;

import static org.junit.Assert.assertEquals;

import org.junit.Test;

import leetcode.ListNode;

public class SolutionTest {
    @Test
    public void testDeleteNodes() {
        //Input: head = [1,2,3,4,5,6,7,8,9,10,11,12,13], m = 2, n = 3
        // Output: [1,2,6,7,11,12]
        ListNode head = new ListNode(1);
        ListNode current = head;
        for (int i = 2; i <= 13; i++) {
            current.next = new ListNode(i);
            current = current.next;
        }
        Solution solution = new Solution();
        ListNode result = solution.deleteNodes(head, 2, 3);
        assertEquals(1, result.val);
        assertEquals(2, result.next.val);
        assertEquals(6, result.next.next.val);
        assertEquals(7, result.next.next.next.val);
        assertEquals(11, result.next.next.next.next.val);
        assertEquals(12, result.next.next.next.next.next.val);
    }
}
package cs497.interviewNOV7;

import static org.junit.Assert.assertEquals;

import org.junit.Test;

import leetcode.ListNode;

public class SolutionTest {
    @Test
    public void testHasCycle() {
        //Input: head = [3,2,0,-4], pos = 1
        //Output: true
        //Explanation: There is a cycle in the linked list, where the tail connects
        //to the 1st node (0-indexed).
        ListNode head = new ListNode(3);
        ListNode node2 = new ListNode(2);
        head.next = node2;
        ListNode node0 = new ListNode(0);
        node2.next = node0;
        ListNode node4 = new ListNode(-4);
        node0.next = node4;
        node4.next = head;

        Solution solution = new Solution();
        boolean result = solution.hasCycle(head);
        assertEquals(true, result);
    }
}
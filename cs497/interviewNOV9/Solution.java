package cs497.interviewNOV9;

import leetcode.ListNode;

// Given the head of a linked list and two integers m and n. Traverse the linked list and remove
// some nodes in the following way:
// Start with the head as the current node.
// Keep the first m nodes starting with the current node.
// Remove the next n nodes
// Keep repeating steps 2 and 3 until you reach the end of the list.

class Solution {
    public ListNode deleteNodes(ListNode head, int m, int n) {
        ListNode current = head;
        ListNode previous = null;
        while (current != null) {
            for (int i = 0; i < m && current != null; i++) {
                previous = current;
                current = current.next;
            }
            for (int i = 0; i < n && current != null; i++) {
                current = current.next;
            }
            previous.next = current;
        }
        return head;
    }
}
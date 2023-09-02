package removenthnode;

class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode start = new ListNode();
        start.next = head;
        ListNode after = start;
        ListNode before = start;

        for (int i = 0; i < n; i++)
            after = after.next;

        while (after.next != null) {
            after = after.next;
            before = before.next;
        }

        before.next = before.next.next;

        return start.next;
    }
}
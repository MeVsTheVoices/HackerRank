from typing import Optional
from leetcode.listnode import ListNode


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (not head) or (not head.next):
            return head

        dummy = ListNode(0)
        dummy.next = head
        previous = dummy
        while head and head.next:
            first = head
            second = head.next

            previous.next = second
            first.next = second.next
            second.next = first

            previous = first
            head = first.next

        return dummy.next
        

# Testing
Testing is at python_testing\swapnodesinpairs_test.py

# Intuition
We use a dummy variable so that we're keeping track of three things, the previous node, the first node, and the second node.

# Approach
    - If the list is empty or has only one node, return the list
    - Create a dummy node and point it at the head
    - Make our dummy node the previous node
    - While the head and the next node exist
        - Make the first node the head
        - Make the second node the next node
        - Make the previous node point at the second node
        - Make the first node point at the second node's next node
        - Make the second node point at the first node
        - Make the previous node the first node
        - Make the head the first node's next node

# Complexity
- Time complexity: O(n)

- Space complexity: O(1)

# Code
```
from typing import Optional


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
        

```
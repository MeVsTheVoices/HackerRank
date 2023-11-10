# Remove Nth Node From End of List
## Problem
Given the head of a linked list, remove the nth node from the end of the list and return its head.


## Intuition
We're given a linked list and asked to remove the nth node from the end of the list. The specification lists O(n) as the time complexity, which is a hint that we should be using a two pointer algorithm. The problem is that we're looking for the nth node from the end of the list, which means we can't just return the node we find, we need to keep searching until we find the nth node from the end of the list.


## Approach
I knew from the start that traversing the list twice wasn't necessary, but trying to figure out how to do it in one pass was a bit tricky. I started by creating a dummy node that points to the head of the list. I then created two pointers, `before` and `after`, and set them both to the dummy node. I then moved `after` n nodes forward. This way, when `after` reaches the end of the list, `before` will be pointing to the node before the nth node from the end of the list. I then set `before.next` to `before.next.next`, which removes the nth node from the end of the list. I then return `dummy.next`, which is the head of the list.


## Complexity
- Time complexity: O(n)
- Space complexity: O(1)

## Code
```java
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
```
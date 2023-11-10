# Intuition
Designed orignally as iterative, redesigned to be recursive

# Approach
Simply as pie. We create a dummy node, then always operate on it's .next, we return the head when both lists are exhausted

# Complexity
- Time complexity: O(n)

- Space complexity: O(n)

# Code
```
class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        if (list1 == null && list2 == null)
            return null;
        ListNode dummy = new ListNode(0);;
        ListNode head = dummy;
        return mergeTwoListsRecursively(list1, list2, dummy, head).next;
    }

    public ListNode mergeTwoListsRecursively(ListNode list1, ListNode list2, ListNode dummy, ListNode head) {
        if (list1 == null && list2 == null)
            return head;
        else if (list1 == null) {
            dummy.next = list2;
            return mergeTwoListsRecursively(null, null, dummy.next, head);
        }
        else if (list2 == null) {
            dummy.next = list1;
            return mergeTwoListsRecursively(null, null, dummy.next, head);
        }
        else {
            if (list1.val < list2.val) {
                dummy.next = list1;
                dummy = dummy.next;
                list1 = list1.next;
            }
            else {
                dummy.next = list2;
                dummy = dummy.next;
                list2 = list2.next;
            }
            return mergeTwoListsRecursively(list1, list2, dummy, head);
        }
    }
}
```
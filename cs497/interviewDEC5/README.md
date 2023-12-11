# Intuition
I've solved this recursively before, but I wanted to try it iteratively this time. We deal with the base cases, and remember that one or the other list can have more members than its complement.

# Approach
- We create a dummy variable to hold the head of the new list.
- We iterate through the lists, adding the smaller value to the new list.
- We return the head of the new list.

# Complexity
- Time complexity: O(n)

- Space complexity: O(n)

# Code
```

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        newList = ListNode()
        head = newList

        if (not list1) and (not list2):
            return None
        elif not list1:
            return list2
        elif not list2:
            return list1
        
        while list1 or list2:
            if list1 and list2:
                if list1.val < list2.val:
                    newList.next = ListNode(list1.val)
                    newList = newList.next
                    list1 = list1.next
                elif list1.val > list2.val:
                    newList.next = ListNode(list2.val)
                    newList = newList.next
                    list2 = list2.next
                else:
                    newList.next = ListNode(list1.val)
                    newList = newList.next
                    newList.next = ListNode(list2.val)
                    newList = newList.next
                    list1 = list1.next
                    list2 = list2.next
            elif list1:
                newList.next = ListNode(list1.val)
                newList = newList.next
                list1 = list1.next
            elif list2:
                newList.next = ListNode(list2.val)
                newList = newList.next
                list2 = list2.next
        return head.next

```
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def from_list(lst):
        if not lst:
            return None
        head = ListNode(lst[0])
        current = head
        for i in range(1, len(lst)):
            current.next = ListNode(lst[i])
            current = current.next
        return head
    
    def __eq__(self, value):
        # Compare the values of the linked list
        current1 = self
        current2 = value
        while current1 and current2:
            if current1.val != current2.val:
                return False
            current1 = current1.next
            current2 = current2.next
        return current1 is None and current2 is None
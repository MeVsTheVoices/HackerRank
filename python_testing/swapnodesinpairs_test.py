import unittest
from leetcode.swapnodesinpairs.solution import Solution
from leetcode.listnode import ListNode

class SwapNodesTest(unittest.TestCase):
    def testSwapPairs(self):
        solution = Solution()
        given = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
        expected = ListNode(2, ListNode(1, ListNode(4, ListNode(3))))
        actual = solution.swapPairs(given)
        self.assertTrue(self.swapPairsHelper(expected, actual))

        given = None
        expected = None
        actual = solution.swapPairs(given)
        self.assertTrue(self.swapPairsHelper(expected, actual))

        given = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        expected = ListNode(2, ListNode(1, ListNode(4, ListNode(3, ListNode(5)))))
        actual = solution.swapPairs(given)
        self.assertTrue(self.swapPairsHelper(expected, actual))

    def swapPairsHelper(self, lhs, rhs):
        lhsHead = lhs
        rhsHead = rhs
        while lhsHead and rhsHead:
            if lhsHead.val != rhsHead.val:
                return False
            lhsHead = lhsHead.next
            rhsHead = rhsHead.next
        if lhsHead or rhsHead:
            return False
        return True
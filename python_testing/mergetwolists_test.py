import unittest
from cs497.interviewDEC5.solution import Solution
from cs497.interviewDEC5.solution import ListNode

class TestSolution(unittest.TestCase):
    def testMergeTwoLists(self):

        sol = Solution()
        # Test 1
        head1 = ListNode(0, ListNode(1, ListNode(1, ListNode(3))))
        head2 = ListNode(0, ListNode(1, ListNode(1, ListNode(3))))
        expected = ListNode(0, ListNode(0, ListNode(1, ListNode(1, ListNode(1, ListNode(1, ListNode(3, ListNode(3))))))))
        actual = sol.mergeTwoLists(head1, head2)
        while expected and actual:
            self.assertEqual(expected.val, actual.val)
            print(expected.val, actual.val)
            expected = expected.next
            actual = actual.next
        self.assertIsNone(expected)
        self.assertIsNone(actual)
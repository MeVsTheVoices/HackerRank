import unittest
from cs497.interviewDEC5.solution import Solution

class TestSolution(unittest.TestCase):
    def testMergeTwoLists(self):
        sol = Solution()
        # Test 1
        list1 = [1,2,4]
        list2 = [1,3,4]
        result = sol.mergeTwoLists(list1, list2)
        expected = [1,1,2,3,4,4]
        self.assertEqual(expected, result)
        # Test 2
        list1 = []
        list2 = []
        result = sol.mergeTwoLists(list1, list2)
        expected = []
        self.assertEqual(expected, result)
        # Test 3
        list1 = []
        list2 = [0]
        result = sol.mergeTwoLists(list1, list2)
        expected = [0]
        self.assertEqual(expected, result)
        
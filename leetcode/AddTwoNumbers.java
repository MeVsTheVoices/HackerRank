package leetcode;

import java.math.BigInteger;

class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        BigInteger multiplier = BigInteger.valueOf(1);
        BigInteger l1Term = new BigInteger(new byte[] {0});
        BigInteger l2Term = new BigInteger(new byte[] {0});
        while(l1 != null || l2 != null) {
            if (l1 != null) {
                l1Term = l1Term.add(multiplier.multiply(BigInteger.valueOf(l1.val)));
                l1 = l1.next;
            }
            if (l2 != null) {
                l2Term = l2Term.add(multiplier.multiply(BigInteger.valueOf(l2.val)));
                l2 = l2.next;
            }
            System.out.println(l1Term + " " + l2Term);
            multiplier = multiplier.multiply(BigInteger.valueOf(10));
        }
        BigInteger sum = l1Term.add(l2Term);
        System.out.println(sum + " " + l1Term + " " + l2Term);
        BigInteger dividend = BigInteger.valueOf(10);
        ListNode root = new ListNode(0);
        ListNode current = root;
        ListNode previous = root;
        for (; (!(sum.mod(dividend)).equals(BigInteger.valueOf(0))) || (sum.compareTo(BigInteger.valueOf(0)) == 1);) {
            BigInteger term = sum.mod(dividend);
            BigInteger value = term.divide(dividend.divide(BigInteger.valueOf(10)));
            System.out.println(sum + " " + value);
            current.val = value.intValue();
            current.next = new ListNode(0);
            previous = current;
            current = current.next;

            sum = sum.subtract(term);
            dividend= dividend.multiply(BigInteger.valueOf(10));
        }
        previous.next = null;
        return root;
    }
}
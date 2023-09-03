package mergeksortedlists;
class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        // there is a more optimum solution than the one I'm about to implement
        // we'd use a priority queue to find the next list to draw elements from
        // and order values based on the list nodes value



        // this is the brute force solution
        // we'll just iterate through all the lists and find the smallest value
        // and add it to the new list
        ListNode result = null;
        ListNode resultHead = null;
        int smallestIndex = -1;
        int smallestValue = Integer.MAX_VALUE;
        boolean done = false;

        while (!done) {
            done = true;
            smallestIndex = -1;
            smallestValue = Integer.MAX_VALUE;
            for (int i = 0; i < lists.length; i++) {
                if (lists[i] != null) {
                    done = false;
                    if (lists[i].val < smallestValue) {
                        smallestValue = lists[i].val;
                        smallestIndex = i;
                    }
                }
            }
            if (smallestIndex != -1) {
                if (result == null) {
                    result = new ListNode(smallestValue);
                    resultHead = result;
                } else {
                    result.next = new ListNode(smallestValue);
                    result = result.next;
                }
                lists[smallestIndex] = lists[smallestIndex].next;
            }
        }
        return resultHead;
    }
}
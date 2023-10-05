# Intuition
There's other intuitive ways to deal with this problem that are infact much faster. However, this was written on a time crunch, and using this method demonstrates the simplest approach well.

# Approach
My approach to this problem is simple, we keep an ArrayList to hold the elements common to both. If we've already seen that an element is in our ArrayList, then we have no work to do. Otherwise, we look through the second list to find an instance, if we find one, we add that to our ArrayList, then continue on to the next element.

# Complexity
- Time complexity: Time complexity: O(n^2)
- We're iterating n times for n elements in an array
- Space complexity: Space complexity: O(n)
- In the worst case, were all elements to be common and unique to both, we'd end up returning a list of n elements

# Code
```
class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        ArrayList<Integer> list = new ArrayList<Integer>();
        for (int i = 0; i < nums1.length; i++) {
            if (list.contains(nums1[i])) {
                continue;
            }
            for (int j = 0; j < nums2.length; j++) {
                if (nums1[i] == nums2[j]) {
                    list.add(nums1[i]);
                    break;
                }
            }
        }
        int[] result = new int[list.size()];
        for (int i = 0; i < result.length; i++)
            result[i] = list.get(i);
        return result;
    }
}
```
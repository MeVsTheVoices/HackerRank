# Median of Two Sorted Arrays
## Problem
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

## Intuition
This was hell. Wrapping my head around the particulars was the stumbling block. I had to draw out the arrays and the indices to get a better understanding of what was going on. I also had to draw out the different cases to make sure I was handling them correctly. I ended up with a giant mess of if statements to handle the edge cases, and ended up seeking help for that end.


## Approach
The trick to this was using an absolute ton of paper to actually wrap my head around what I was trying to do. Once I got that subtracted the median of the smaller from the size of the two, I started to make progress. I found a trick online to help condense my work. Assigning maximum and minimum integer values to the left and right of the median of the smaller array, and the median of the larger array, I could compare the left and right of the smaller and larger arrays to see if they were in the right place. If they were, I could return the median. If not, I could adjust the indices of the smaller array to get closer to the median. I had to do a lot of work to make sure I was handling the edge cases correctly, but I got there in the end.


## Complexity
- Time complexity: O(log(min(m, n)))
- Space complexity: O(1)

## Code
```java
    class Solution {
        public double findMedianSortedArrays(int[] nums1, int[] nums2) {
            int[] smaller = nums1.length < nums2.length ? nums1 : nums2;
            int[] larger = nums1.length < nums2.length ? nums2 : nums1;

            int sizeOfBoth = smaller.length + larger.length;
            int medianIndex = sizeOfBoth / 2;

            int a = 0;
            int b = smaller.length - 1;

            while(true) {
                int i = Math.floorDiv((a + b), 2);
                int j = medianIndex - i - 2;

                int smallerLeft = i >= 0 ? smaller[i] : Integer.MIN_VALUE;
                int smallerRight = (i + 1) < smaller.length ? smaller[i + 1] : Integer.MAX_VALUE;
                int largerLeft = j >= 0 ? larger[j] : Integer.MIN_VALUE;
                int largerRight = (j + 1) < larger.length ? larger[j + 1] : Integer.MAX_VALUE;

                if (smallerLeft <= largerRight && largerLeft <= smallerRight) {
                    if ((sizeOfBoth % 2) != 0)
                        return (double) Math.min(largerRight, smallerRight);
                    else   
                        return (double) (Math.max(smallerLeft, largerLeft) + Math.min(smallerRight, largerRight)) / 2;
                }
                else if (smallerLeft > largerRight)
                    b = i - 1;
                else
                    a = i + 1;
            }
        }
    }
```
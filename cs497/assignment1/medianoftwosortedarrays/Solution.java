package cs497.assignment1.medianoftwosortedarrays;

class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        // sort arrays by size
        int[] smaller = nums1.length < nums2.length ? nums1 : nums2;
        int[] larger = nums1.length < nums2.length ? nums2 : nums1;

        int sizeOfBoth = smaller.length + larger.length;
        int medianIndex = sizeOfBoth / 2;

        // indices for smaller array
        int a = 0;
        int b = smaller.length - 1;

        while(true) {
            // we're keeping two pointers here, i for the smaller, j for the larger
            int i = Math.floorDiv((a + b), 2);
            // if we take the middlepoint of the smaller array, then subtract that from the halfway point of both
            int j = medianIndex - i - 2;

            // saving myself from getting in to hell with if statements and losing my track
            int smallerLeft = i >= 0 ? smaller[i] : Integer.MIN_VALUE;
            int smallerRight = (i + 1) < smaller.length ? smaller[i + 1] : Integer.MAX_VALUE;
            int largerLeft = j >= 0 ? larger[j] : Integer.MIN_VALUE;
            int largerRight = (j + 1) < larger.length ? larger[j + 1] : Integer.MAX_VALUE;

            // if the median we found in the smaller array is less than equal to the +1 in the larger
            // and the median we found in the larger array is less than or equal to the +1 in the smaller
            if (smallerLeft <= largerRight && largerLeft <= smallerRight) {
                // for an even sized
                if ((sizeOfBoth % 2) != 0)
                    // the smaller of the right partitions is our answer
                    return (double) Math.min(largerRight, smallerRight);
                else   
                    // otherwise, the median is the smaller of the right partitions, and the larger of the left partitions
                    return (double) (Math.max(smallerLeft, largerLeft) + Math.min(smallerRight, largerRight)) / 2;
            }
            else if (smallerLeft > largerRight)
                // if the median of the left partition is larger than the right +1
                // move the upper bound of the smaller partition down one
                // then try again
                b = i - 1;
            else
                // if the median of the left partition is less than or equal to that of the +1
                // move the lower bound of the smaller partition up one
                // then try again
                a = i + 1;
        }
    }
}
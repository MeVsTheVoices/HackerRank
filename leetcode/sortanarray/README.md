# Intuition
It's merge sort, baby!

# Approach
We under take several steps
- We call a recursive function with pointers to the start and the end of the array
- If the two pointers are pointing to the same element, we return that element as an array
- Otherwise, we break the array in half, then call our recursive function on both halves of the array
- Then, we call our merge function
    - Our merge function takes whichever element in the left array or right array is smaller, and adds that to the return value
    - If the right array or left array is larger than its counterpart, then we take the remaining elements and append them to our return value

# Complexity
- Time complexity: O(n*log(n))
    - We merge n times on an array broken in to log(n) parts

- Space complexity: O(n)
    - There is no overlap in creating the sub arrays, but this is bounded

# Code
```
class Solution {
    public int[] sortArray(int[] nums) {
        return mergeSort(nums, 0, nums.length - 1);
    }

    private int[] mergeSort(int[] nums, int start, int end) {
        if (start == end) {
            return new int[] {nums[start]};
        }
        int mid = (start + end) / 2;
        int[] left = mergeSort(nums, start, mid);
        int[] right = mergeSort(nums, mid + 1, end);
        return merge(left, right);
    }

    private int[] merge(int left[], int right[]) {
        int[] result = new int[left.length + right.length];
        int i = 0, j = 0, k = 0, l = 0;
        while ( i < left.length && j < right.length) {
            if (left[i] < right[j])
                result[k++] = left[i++];
            else
                result[k++] = right[j++];
        }
        while (i < left.length)
            result[k++] = left[i++];
        while (j < right.length)
            result[k++] = right[j++];

        return result;
    }
}
```
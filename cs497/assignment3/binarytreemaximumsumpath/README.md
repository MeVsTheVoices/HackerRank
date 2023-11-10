# Intuition
The intiution behind this is simple. If we go both ways from a node, then we can't return to the parent node, if this is greater than the greatest sum we've gotten, we update a class variable, otherwise, we return the greatest of the paths, and work recursively.

# Approach
My first attempt worked for the vast majority of cases, but, exceeded time limits for the largest case, so, I threw memoization at the solution in a naive attempt to speed things up.

# Complexity
- Time complexity: O(log(n))

- Space complexity: O(n)

# Code
```java
class Solution {
    private int currentMax = Integer.MIN_VALUE;
    private Map<TreeNode, Integer> memo = new HashMap<>();
    
    public int maxPathSum(TreeNode root) {
        currentMax = Integer.MIN_VALUE;
        maxPathSumHelper(root);
        return currentMax;
    }

    private int maxPathSumHelper(TreeNode start) {
        if (start == null)
            return 0;

        if (memo.containsKey(start))
            return memo.get(start);

        int left = maxPathSumHelper(start.left);
        int right = maxPathSumHelper(start.right);

        int mostIfSplit = left + right + start.val;
        int mostIfNotSplit = Math.max(left, right) + start.val;

        int result = Math.max(mostIfSplit, Math.max(mostIfNotSplit, start.val));
        currentMax = Math.max(result, currentMax);
        memo.put(start, result);

        return Math.max(Math.max(left, right), 0) + start.val;
    }
}
```